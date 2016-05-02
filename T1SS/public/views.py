from T1SS import app
from T1SS.Tarea1 import CbcMac, AesEcrypt
from T1SS.forms.tester import TestForm
from T1SS.forms.validate import ValidateForm
from T1SS.models.user import User
from flask import render_template, redirect, url_for, request, flash


@app.route('/tester', methods=['GET', 'POST'])
def tester():
    form = TestForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.user_name == form.user_name.data).first()
        if not user:
            flash("Usuario no registrado")
        else:
            # Revisar si texto es múltiple de 16
            key = eval(user.aes_key)
            iv, c = AesEcrypt(form.text.data, key)
            flash("IV: " + str(iv))
            flash("Cifrado: " + str(c))
            flash("Mac: " + str(CbcMac(form.text.data, key)))
        return redirect(url_for('tester'))
    else:
        return render_template('tester.html', form=form)


@app.route('/validator')
def validator():
    form = ValidateForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.user_name == form.user_name.data).first()
        if not user:
            flash("Usuario no registrado")
        else:
            # Revisar si texto es múltiple de 16
            key = eval(user.aes_key)
            mac = eval(form.tag)
            flash("Mac: " + str(CbcMac(form.text.data, key)))
        return redirect(url_for('tester'))
    else:
        return render_template('validator.html')


@app.route('/')
def home():
    return redirect(url_for('tester'))