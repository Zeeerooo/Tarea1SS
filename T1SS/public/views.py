from T1SS import app
from T1SS.Tarea1 import CbcMac, AesEcrypt
from T1SS.forms.tester import TestForm
from T1SS.forms.validate import ValidateForm
from T1SS.models.used_word import UsedWord
from T1SS.models.user import User
from flask import render_template, redirect, url_for, request, flash


@app.route('/tester', methods=['GET', 'POST'])
def tester():
    form = TestForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.user_name == form.user_name.data).first()
        word = eval(form.text.data)
        if not user:
            error = "Usuario no registrado"
            form.user_name.errors.append(error)
            return render_template('tester.html', form=form)

        elif user.used_words.count() >= 50:
            error = "Usted completó la cantidad máxima de consultas."
            form.user_name.errors.append(error)
            return render_template('tester.html', form=form)

        elif not len(word) % 16 == 0:
            error = "Texto debe ser múltiplo de 16."
            form.text.errors.append(error)
            return render_template('tester.html', form=form)

        else:
            key = eval(user.aes_key)
            iv, c = AesEcrypt(word, key)

            # Agrego palabra a las ya probadas
            UsedWord.store_if_no_exist(str(word), user)

            flash("IV: " + str(iv))
            flash("Cifrado: " + str(c))
            flash("Mac: " + str(CbcMac(word, key)))
            flash("A usted le quedan " + str(50 - user.used_words.count()) + " consultas")
            return redirect(url_for('tester'))
    else:
        return render_template('tester.html', form=form)


@app.route('/validator', methods=['GET', 'POST'])
def validator():
    form = ValidateForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.user_name == form.user_name.data).first()
        word = eval(form.text.data)
        # Crear usuario test para que no peudan robar cosas
        if not user:
            error = "Usuario no registrado"
            form.user_name.errors.append(error)
            return render_template('validator.html', form=form)

        elif not len(word) % 16 == 0:
            error = "Texto debe ser múltiplo de 16."
            form.text.errors.append(error)
            return render_template('validator.html', form=form)

        elif user.used_words.filter(UsedWord.word == str(word)).first():
            error = "Usted ya testeo esta palabra!"
            form.text.errors.append(error)
            return render_template('validator.html', form=form)
        else:
            # Revisar si texto es múltiple de 16
            key = eval(user.aes_key)
            mac = eval(form.tag.data)
            if CbcMac(word, key) == mac:
                flash("¡Falsificación exitosa!")
                user.validateHomework()
                return redirect(url_for('.validator'))
            else:
                error = "¡Fallaste! Vuelve a intentar"
                form.tag.errors.append(error)
                return render_template('validator.html', form=form)
    else:
        return render_template('validator.html', form=form)


@app.route('/')
def home():
    return redirect(url_for('tester'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
