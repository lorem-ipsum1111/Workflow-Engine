from flask import Flask, render_template, url_for, request, session, redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'JRTTYjetKINs'


example_string = "[{\"type\":\"checkbox-group\",\"required\":false,\"label\":\"Checkbox Group\",\"toggle\":false,\"inline\":false,\"name\":\"checkbox-group-1587731883304\",\"access\":false,\"other\":false,\"values\":[{\"label\":\"Option 1\",\"value\":\"option-1\",\"selected\":true}]},{\"type\":\"hidden\",\"name\":\"hidden-1587731883988\",\"access\":false},{\"type\":\"select\",\"required\":false,\"label\":\"Select\",\"className\":\"form-control\",\"name\":\"select-1587731884978\",\"access\":false,\"multiple\":false,\"values\":[{\"label\":\"Option 1\",\"value\":\"option-1\",\"selected\":true},{\"label\":\"Option 2\",\"value\":\"option-2\"},{\"label\":\"Option 3\",\"value\":\"option-3\"}]}]"


@app.route('/')
def index():
    return render_template('genericHomePage.html')

@app.route('/workflowEditor', methods=['POST', 'GET'])
def workflowEditor():
    if request.method == 'POST':
        JSONformLayout = request.form['custId']
        session['formdata'] = JSONformLayout
        print(JSONformLayout)

        JSONworkflowNodes = request.form['workflow_nodes']
        print(JSONworkflowNodes)

        JSONworkflowDetails = request.form['workflow_details']
        print(JSONworkflowDetails)

    admins = ["admin1", "admin2", "admin3", "admin4", "admin5"]#this thing will be fetched from database
    role_dept = [["role_1","dept_1"],["role_2","dept_2"],["role_3","dept_3"],["role_4","dept_4"],["role_5","dept_5"]]#also fetched from the database
    roles = ["role_1","role_2","role_3","role_4","role_5"]#roles without any dept also fetched from the database
    return render_template('workflowEditor.html', admins = admins, role_dept = role_dept, roles = roles)#the list of all ppl at all roles will be passed from here...

@app.route('/formBuilder')
def formBuilder():
    return render_template('formbuilder.html')

@app.route('/initiateProcess', methods=['GET','POST'])
def showProcesses():
    # permissibleWorkflows=['Budget Allocation','Leave application','Ticket Reimbursement']
    workflowForms=[example_string, example_string, example_string]
    if request.method == 'GET':
        return render_template('processInit.html', permissibleWorkflows=['Budget Allocation','Leave application','Ticket Reimbursement'])
    workflowIndex = request.form['processId']
    session['jsonForm'] = workflowForms[int(workflowIndex)]
    return redirect(url_for('fillForm', type='processInit'))


@app.route('/initiateTask', methods=['GET','POST'])
def showTasks():
    # permissibleWorkflows=['Budget Allocation','Leave application','Ticket Reimbursement']
    taskForms=[example_string, example_string, example_string]
    if request.method == 'GET':
        return render_template('executeTask.html', availableTasks=['Approve budget','Approve leave','Release funds'])
    taskIndex = request.form['taskId']
    session['jsonForm'] = taskForms[int(taskIndex)]
    return redirect(url_for('fillForm', type='task'))

@app.route('/fillForm', methods=['GET','POST'])
@app.route('/fillForm/<string:type>', methods=['POST','GET'])
def fillForm(type):
    # return render_template('fillForm.html',jsonFormData=session['jsonForm'], formType = type)
    if request.method == 'GET':
        return render_template('fillForm.html',jsonFormData=session['jsonForm'], formType = type)
    userResponse = request.form['response']
    if type == 'processInit':
        session['processInitResponse'] = userResponse
    session['taskResponse'] = userResponse
    return redirect(url_for('index'))

@app.route('/node_configuration')
def node_configuration():
    return node_configuration()    

if __name__ == '__main__':
    app.run()
