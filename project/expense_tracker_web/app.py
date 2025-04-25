from flask import Flask, render_template, request, redirect
app = Flask(__name__)
expenses = []
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/add', methods=['get','POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = float(request.form['amount'])
        expenses.append({"name": name, "amount": amount})
        return redirect('expenses')
    return render_template('add.html')
@app.route('/expenses')
def view_expenses():
    total = sum(expense['amount'] for expense in expenses)
    return render_template('expenses.html', expenses=expenses, total=total)
if __name__ == '__main__':
    app.run(debug=True)