from flask import Flask, render_template, redirect, url_for, request, session
from Foodfix import dishes
from forms import SelectForm, FixForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'keinemehrbisous'


#app route shows what to return with different url paths and the corresponding pages
@app.route('/')
def index():
    #html file is linked
    return render_template('home.html')


@app.route('/search')
def Search():
    return render_template('Searchy.html')


#Tells what methods to use
@app.route('/fix', methods=['GET', 'POST'])
def Fix():
    selected = None
    # form is set as unselected
    form = SelectForm()
    if form.validate_on_submit():
        selected = form.selected.data
        session['selected'] = form.selected.data
        form.selected.data = ''
        return redirect(url_for('Problem'))
    return render_template('Fixy.html', dishes=dishes, form=form)


@app.route('/fix/problem', methods=['GET', 'POST'])
def Problem():
   form = FixForm()

   if form.validate_on_submit():
       problem = form.problem.data
       session['problem'] = problem
   return render_template('FixForm.html')


#makes sure that we're in debugging mode during app run
if __name__ == '__main__':
    app.run()
    app.run(debug=True)
    app.run(debug=False)
