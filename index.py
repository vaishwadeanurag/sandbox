id_count = 0
class Patient:
	def __init__(self,**kwarg):
		global id_count
		id_count +=1
		self.mbr_id = id_count
		self.name = kwarg["name"]
		self.gender = kwarg["gender"]
		self.age = kwarg["age"]
		self.address = kwarg["address"]
		self.phone = kwarg["phone"]

	def read(self):
		return "".join(["Patient Informations\n","Id : ",str(self.mbr_id),"\nName : ",self.name,"\nGender : ",self.gender,"\nAge : ",self.age,"\nAddress : ",self.address,"\nPhone : ",self.phone ])

	def update(self,**kwarg):
		self.name = kwarg["name"]
		self.gender = kwarg["gender"]
		self.age = kwarg["age"]
		self.address = kwarg["address"]
		self.phone = kwarg["phone"]


from bottle import get, post, request,route, run, template,put,delete
pat_dict = {}

@route('/')
@route('/patient')
def patient():
    return '<b>Patient is working fine do somthing with it /create,/update,/delete</b>!'

@post('/patient')
def create():
	name = request.POST['name']
	gender = request.POST['gender']
	age = request.POST['age']
	address = request.POST['address']
	phone = request.POST['phone']
	temp_pat = Patient(name = name,gender = gender,age = age,address = address,phone = phone)
	pat_dict.update({str(temp_pat.mbr_id):temp_pat})
	return '<b>Patient Created with ID {0}'.format(temp_pat.mbr_id)

@get('/patient/<id>')
def read(id):
	return pat_dict[id].read()

@put('/patient/<id>')
def update(id):
	mbr_id = request.POST['mbr_id']
	if mbr_id != id:
		return "Access Denied"
	pat_dict[id].update(name = request.POST['name'],gender = request.POST['gender'],age = request.POST['age'],address = request.POST['address'],phone = request.POST['phone'])
	return "Updated Sucessfully ".join([str(mbr_id)])

@delete('/patient/<id>')
def delete(id):
	del(pat_dict[id])
	return "Deleted Sucessfully {0}".format(id)

run(host='0.0.0.0', port=8080)