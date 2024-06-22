class User:
    def __init__(self, name, address, email, password, job_title):
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        self.job_title = job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.job_title = new_job_title

    def get_user_info(self):
        print(f'User {self.name} working as {self.job_title} lives in {self.address}. You can contact them at {self.email}')
