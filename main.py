# app made by Laaledesiempre
#   This is just for educational porpuse, i don't consent other usages
#       the images that this aplication brings could have Copyright, please don't use images without authors consent.
#   Have a nice day
# surfing web is cool c:

import requests # https://docs.python-requests.org/en/v2.0.0/
from bs4 import BeautifulSoup as bs # https://tedboy.github.io/bs4_doc/

# Functions
def print_empty_line():
  "Prints empty line (just for code readability)"
  print("")

def press_to_continue(message="press ENTER to continue "):
  """Makes a input with custom message (just for code readability)

  @params:
    message:string -> message for the input
  """
  input(message)

def scrap_pinterest_image(url):
  """This function use and pinterest URL to search common pinterest's image attrs and returns that image URL

  @params:

    url:string -> a valid Pinterest post URL
      example: "https://ar.pinterest.com/pin/29554941298312230/"

  @returns:

    image_url:string -> a Pinterest image URL
      example: "https://i.pinimg.com/736x/aa/9a/95/aa9a952b78a2db09a19d85f280ce6fb3.jpg"

  """
  response = requests.get(url)
  html = response.text
  page=bs(html,"html.parser")
  element_scrapped=page.find("img",attrs={"fetchpriority":"auto","loading":"auto"})
  return element_scrapped.attrs["src"]

# End of functions

# ---

# Program

while True:
  # Menu
  print("Pinterest web scrapper :3")
  print("""
    What do yo tant to do?
    1) Scrapppppp
    2) Download many :3
    S) Exit
  """)
  response = input("Option: ")

  # Responses:
  if response == "1": # 1
    while True:

      url = input("Paste the URL or write s to skip: ")

      if url.lower() == "s":
        break

      try:
        link = scrap_pinterest_image(url)
        print("Your link is:", link )

        print("Want to download?")
        while True:
          response = input("[y/n]: ")

          if response[0].lower() == "y":

            name_for_file = link[-10:]
            open(name_for_file, 'wb').write(requests.get(link).content)
            print(f"file {name_for_file} Downloaded succesfully")
            break

          elif response[0].lower() == "n":
            break

          else:
            print("Not a valid option :/")

        press_to_continue()
        break

      except Exception as error:

        print("""
  Something went wrong, if problem persist make an issue on Github
        """)

        print("\tError message (may help c: ):")
        print("\t\t", error)
        print_empty_line()

  elif response == "2": #2
    
    print("In this mode, you can put all the links you want one by one, and it will download automaticaly")

    while True:
        url= input("Paste the URL or write s to skip: ")

        if url.lower() == "s":
          break
        
        try:
          link = scrap_pinterest_image(url)
          name_for_file = link[-10:]
          open(name_for_file, 'wb').write(requests.get(link).content)
          print(f"file {name_for_file} Downloaded succesfully")
        except Exception as error:
            print("""
    Something went wrong, if problem persist make an issue on Github
            """)

            print("\tError message (may help c: ):")
            print("\t\t", error)
            print_empty_line()


  elif response.lower() == "s": # S
    break

  else: # else
    print("Thats not a valid option pal :c")
    press_to_continue()

