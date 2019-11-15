from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class CreatingFolder:
    # to get the environment directory
    environ_file_path = os.environ.get('ONEDRIVE')

    def __init__(self, project_name):
        self.project_name = project_name

    # to create the project folder
    def create_project_folder(self):
        file_name = f'Documents/{self.project_name}'
        project_location = os.path.join(self.environ_file_path, file_name)
        if not os.path.exists(project_location):
            os.makedirs(project_location)
        return project_location


class CreateRepoGitLocal(CreatingFolder):
    content = 'dummy content'
    def __init__(self, project_name):
         CreatingFolder.__init__(self, project_name)

    def creating_readme(self):
        folder_name = super().create_project_folder()
        with open(os.path.join(folder_name, 'readme.md'), 'w') as f:
            f.write(self.content)

class AutomatingGit(CreateRepoGitLocal):
    # Chrome driver that opens up the browser
    driver = webdriver.Chrome("../drivers/chromedriver")

    def __init__(self, project_name, url_site, userName, pswd):
        CreateRepoGitLocal.__init__(self, project_name)
        self.url_site = url_site
        self.userName = userName
        self.pswd = pswd

    def github_sign_in_page(self):
        self.driver.get(self.url_site)
        sign_in =  self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()
        return sign_in
    
    def adding_credentials(self):
        self.github_sign_in_page()
        self.driver.execute_script('''
            window.document.querySelector("#login_field").value = arguments[0];
            window.document.querySelector("#password").value = arguments[1];
            window.document.querySelector(".btn.btn-primary.btn-block").click()
        ''', self.userName, self.pswd)

    def creating_git_repo_remote(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[6]/details/summary").click()
        self.driver.find_element(By.XPATH, "/html/body/div[1]/header/div[6]/details/details-menu/a[1]").click()
        self.driver.execute_script('''
            window.document.querySelector("#repository_name").value = arguments[0]
        ''', self.project_name)
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="new_repository"]/div[3]/button').click()

    def running_all_fun(self):
        CreateRepoGitLocal(self.project_name).creating_readme()
        self.adding_credentials()
        self.creating_git_repo_remote()

# shell scripting
class GitCommands(CreatingFolder):
    def __init__(self, project_name):
        CreatingFolder.__init__(self, project_name)
        
    def path_name(self):
        return CreatingFolder(self.project_name).create_project_folder()

    def redirect_to_project_folder(self):
        # Runs below shell script using os module
        time.sleep(2)
        os.chdir(self.path_name())
        os.system('git init')
        os.system('git add -A')        
        os.system('git commit -m "initial commit"')
        time.sleep(10)
        os.system(f'git remote add origin https://github.com/joydeep181992/{self.project_name}.git')
        time.sleep(10)
        os.system('git push origin master')


project_name = input("Project Name: ")
url = "https://github.com/"
userName = input("User Name: ")
pswd = input("Password: ")

git_instance = AutomatingGit(project_name, url, userName, pswd)   
git_instance.running_all_fun()

git_cmds = GitCommands(project_name)
git_cmds.redirect_to_project_folder()