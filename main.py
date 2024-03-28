import pandas as pd
df =pd.read_csv('confirmedList.csv')
matrix2 = df[df.columns[0]].to_numpy()
list1 = matrix2.tolist()
print("The Selected Emails are: ")
print(list1)


# Email Component ---------------------------------------------
from redmail import gmail
with open('template.html', 'r') as template:
    html_string = template.read()

#Set the Email and password ( VERY IMPORTANT!!!)
gmail.username = ''
gmail.password = ''

for reciever in list1:
    gmail.send(
        #Subject and #Text ( This is the thumbnail text )
        subject = "Confirmation of Attendance",
        receivers = reciever,
        text="for the workshop : leadership skills make sure to make your attendance clear for the upcoming workshop",
        html= html_string,
        body_images={
            'my_image1': 'test1.jpg',
            'my_image3': 'test3.jpg',
            #This is the Workshop Image that can be changed below
            'my_image2': 'image2.jpeg',
        },

        #Contents of the Email
        body_params={
            'title': "Confirmation of Attendance",
            'subtitle': "Workshop : Leadership Skills",
            'body_line1': 'We are looking forward to seeing you in the upcoming workshop and learning together.',
            'body_line2': 'Please confirm your attendance by pressing the button below: ',

            #To Hide the button, set hide_button to 'hidden' and link to an empty String.
            'hide_button': '',
            'link': 'https://forms.gle/aTG2ChsSazLwPZpK8'


        }



    )

print("All emails have been sent successfully.")