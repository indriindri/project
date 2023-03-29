import os
import json
from getpass import getpass

from settings import Settings
from user import User
from drama import Drama

class DramaListApp:

	def __init__(self):
		self.settings = Settings()
		#self.active = True

	def load_data(self):
		try:
			with open(self.settings.dramas_location, 'r') as file:
				self.settings.dramas = json.load(file)
		except:
			self.settings.dramas = {}

		try:
			with open(self.settings.users_location, 'r') as file:
				self.settings.users = json.load(file)
		except:
			self.settings.users = {}
		#print(self.settings.dramas, self.settings.users)

	def clear_screen(self):
		if os.name == "nt":
			os.system("cls")
		else:
			system("clear")

	def logger(self):
		#self.user = User(username="admin", first="Admin", last="Admin", password="12345")
		#return True
		self.clear_screen()
		self.login_attempts = 0
		while self.login_attempts < 3:
			print("\nPlease Login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.users:
				if self.settings.users[username]["password"] == password:
					self.user = User(username,
						first=self.settings.users[username]['first'],
						last=self.settings.users[username]['last'],
						password="")
					return True
			else:
				print("Login Failed.")
			self.login_attempts += 1

		return False

	def show_menus(self):
		self.clear_screen()
		print(self.settings.menu)

	def find_dramas(self, title):
		dramas = self.settings.dramas
		if title in dramas:
			print("Drama found ! ")
			print(f"Title: {title}")
			print(f"Actress : {dramas[title]['actress']}")
			print(f"Episodes : {dramas[title]['episodes']}")
			return True
		else:
			print("Drama doesn't exists, please try again.")

	def save_data(self):
		with open(self.settings.dramas_location, 'w') as file:
			json.dump(self.settings.dramas, file)

	def check_option_user(self, char):
		if char == 'q':
			self.settings.active = False
		elif char == "1":
			self.clear_screen()
			#print(self.settings.dramas)
			dramas = self.settings.dramas 
			print(f"Judul\t\t\t\tAktor\t\t\t\tAktris\t\t\t\tEpisode")

			for title, drama in dramas.items():
				print(f"{title}\t\t\t{drama['actor'].title()}\t\t\t{drama['actress'].title()}\t\t\t{drama['episodes']} ")

			input("Press Enter to Return.")

		elif char == "2":

			self.clear_screen()
			title = input("Enter drama title : ")

			self.find_dramas(title)

			input("Press Enter to Return.")

		elif char == "3":

			self.clear_screen()
			title = input("Title : ")
			actor = input("Actor : ")
			actress = input("Actress : ")
			episodes = input("Total Episodes : ")

			drama = Drama(title, actor, actress, episodes)
			self.settings.dramas[drama.title] = {
				"actor" : drama.actor,
				"actress" : drama.actress,
				"episodes" : drama.episodes
			}

			self.save_data()

			print("New Drama saved.")
			input("Press Enter to Return.")

		elif char == "4":

			self.clear_screen()
			title = input("Title : ")

			if self.find_dramas(title):
				print("Edit\n1.Title  2. Actor  3. Actress  4. Episodes")
				option = input("Whick data do you want to edit/update ? (1/2/3/4)")
				if option == "1":

					old_drama = self.settings.dramas[title]
					new_title = input("New title : ")

					self.settings.dramas[new_title] = {
						"actor" : old_drama["actor"],
						"actress" : old_drama["actress"],
						"episodes" : old_drama["episodes"]
					} 

					del self.settings.dramas[title]
					self.save_data()
					print("New title saved.")

				elif option == "2":

					new_actor = input("New actor : ")
					self.settings.dramas[title]["actor"] = new_actor
					self.save_data()
					print("New actor name saved.")

				elif option == "3":
					new_actress = input("New actress : ")
					self.settings.dramas[title]["actress"] = new_actress
					print("New actress name saved")

				elif option == "4":
					new_episodes = input("New episodes : ")
					self.settings.dramas[title]["episodes"] = new_episodes
					self.save_data()
					print("New episodes saved.")

		elif char == "5":

			self.clear_screen()
			title = input("Title : ")

			if self.find_dramas(title):
				confirm = input("Are you sure to delete this drama ? (y/n)")
				if confirm.lower() == "y":
					del self.settings.dramas[title]

					self.save_data()
					print("Drama deleted.")

			input("Press Enter to Return.")

	def run(self):
		self.load_data()
		if self.logger():
			self.settings.active = True

		while self.settings.active:
			self.show_menus()
			self.check_option_user(input("Option: ").lower())

if __name__ == '__main__':
	app = DramaListApp()
	app.run()