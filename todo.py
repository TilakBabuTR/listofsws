# Create To do app, table should have ID, Date, Task Name, Description and Status
# By default status should be incomplete and date should be today's date


import sys
import sqlite3
import texttable as tt
from datetime import date

conn=sqlite3.connect('todo.db')
c=conn.cursor()
c.execute("CREATE TABLE if not exists todo(taskID integer, taskdate date, taskname text, taskdescription text, taskstatus text, primary key(taskID));")
class Todo:
	with conn:
		try:
			def insert(self):
				print("Do you have task details?")

				# ID=int(input("task ID: "))
				# c.execute("SELECT * from todo where taskid= taskid", {'taskid':ID})
				# count=len(c.fetchall())
				# if count!=0:
				# 	print("Task ID Already Exists. Please enter another ID")
				# 	td.task()
				c.execute("SELECT * from todo")
				rowcount=len(c.fetchall())
				ID=rowcount+1
				Date=input("Enter the Task Date in the given format YYYY-MM-DD--> ")
				if Date=='':
					Date=date.today()
				Title=input("Task Title: ")
				Description=input("Task Description: ")
				Status=input("Status: Complete or Incomplete--> ")
				if Status=='':
					Status='Incomplete'
				c.execute("INSERT into todo values(:id, :taskdate, :title, :description, :status)", {'id': ID, 'taskdate':Date, 'title':Title, 'description':Description, 'status':Status})
				conn.commit()
				c.execute("Select * from todo")
				print(c.fetchall())
				td.task()
		except IntegrityError:
			print("Task ID Already Exists. Please enter another ID")

	def view(self):
		table=tt.Texttable()
		with conn:
			try:
				c.execute("SELECT * from todo")
				obj=c.fetchall()
				count=len(obj)
				if count==0:
					print("No tasks to display")
				else:

					tasklist=[["Task ID", "Task Date", "Task Title", "Task Description", "Task Status"]]
					i=0
					for i in range(0,count):
						rows=[obj[i][0], obj[i][1], obj[i][2], obj[i][3], obj[i][4]]
						tasklist.append(rows)
						i=i+1

					table.add_rows(tasklist)
					print(table.draw())
				td.task()
			except:
				print("Tasks cannot be displayed..........")

		return 0
	def updateTask(self):
		try:
			with conn:
				c.execute("SELECT * from todo")
				obj=c.fetchall()
				count=len(obj)
				if count==0:
					print("No tasks to update")
				else:
						
					c.execute("SELECT taskID, taskname from todo")
					print(c.fetchall())
					uid=int(input("Enter the task ID you want to update: "))
					c.execute("Select * from todo where taskid=:id", {'id':uid})
					tsk=c.fetchall()
					if tsk!=[]:
						udescription=input("Enter the description you want to update: ")
						c.execute("UPDATE todo set taskdescription=:description where taskID=:id", {'description':udescription, 'id':uid})
						conn.commit()
						td.view()
					else:
						print("Task ID doesn't exists")
				td.task()
		except:
			print("Something went wrong")
			td.task()

	def updateStatus(self):
		try:
			with conn:
				c.execute("SELECT * from todo")
				obj=c.fetchall()
				count=len(obj)
				if count==0:
					print("No tasks to update")
				else:

					c.execute("SELECT taskID, taskname, taskstatus from todo")
					td.view()
					uid=int(input("Enter the task ID, which status need to be changed: "))
					c.execute("SELECT * from todo where taskID=:id", {'id': uid})
					tsk2=c.fetchall()
					if tsk2!=[]:
						ustatus=input("Please change the status to Complete or Incomplete --> ")
						c.execute("UPDATE todo set taskstatus=:status where taskID=:id", {'status': ustatus, 'id': uid})
						conn.commit()
						td.view()
					else:
						print("Task ID doesn't exists")
				td.task()
		except:
			print("Something went wrong")

	def exit(self):
		sys.exit("Complete your tasks ASAP. Ignore if all tasks are complete")

	try:
		def task(self):
			print("Enter 1 to Add the New Task")
			print("Enter 2 to View the Tasks and Status")
			print("Enter 3 to Update the Task")
			print("Enter 4 to Update the Task Status")
			print("Enter 0 to exit the application")
			task=int(input())
			if task==1:
				td.insert()
			if task==2:
				td.view()
			if task==3:
				td.updateTask()
			if task==4:
				td.updateStatus()
			if task==0:
				td.exit()
				
	except:
		print("Select valid operation")



td=Todo()
td.task()

