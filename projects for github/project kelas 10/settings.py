
class Settings:

	def __init__(self):
		self.active = False
		self.dramas_location = "data/dramas.json"
		self.users_location = "data/users.json"

		self.dramas = None 
		self.users = None 

		self.menu = """
*CURRENTLY WATCHING DRAMAS INFORMATION*
1. VIEW ALL DRAMAS
2. FIND DRAMA BY THE TITLE
3. ADD NEW DRAMA
4. UPDATE DRAMA
5. REMOVE DRAMA THAT HAS BEEN WATCHED
Q. EXIT
"""