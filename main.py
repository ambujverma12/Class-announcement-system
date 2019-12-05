from gtts import gTTS
from datetime import datetime
import pandas as pd
from playsound import playsound
import calendar
#For monday
def Monday():
     df=pd.read_excel(r'D:\my_python\Time_table\Monday.xlsx')

     for i in range(0,4):
   
        for j in range(0,4):
       
             myText=str(df.iloc[i,j])
             language='en'
             if j==0:
                     mySoundA=gTTS(text='  Today is a Class of  '+" "+myText, lang=language, slow=False)
                     mySoundA.save(f"Sound{i}{j}.mp3")
             elif j==1:
                     mySound_2=gTTS(text=' From  '+" "+myText,lang=language,slow=False)
                     mySound_2.save(f"Sound{i}{j}.mp3")
             elif j==2:
                     mySound_3=gTTS(text=' To  '+" "+myText,lang=language,slow=False)  
                     mySound_3.save(f"Sound{i}{j}.mp3")
             elif j==3:
                     mySound_4=gTTS(text='  By  '+" "+myText,lang=language,slow=False)
                     mySound_4.save(f"Sound{i}{j}.mp3")   
     for i in range(0,4):
         for j in range(0,4):
             playsound(r'D:\my_python\Time_table\Sound{}{}.mp3'.format(i,j))
#For Tuesday     
def Tuesday():
     df=pd.read_excel(r'D:\my_python\Time_table\Tuesday.xlsx')

     for i in range(0,4):
   
        for j in range(0,4):
       
             myText=str(df.iloc[i,j])
             language='en'
             if j==0:
                  mySoundA=gTTS(text='  Today is a Class of  '+" "+myText, lang=language, slow=False)
                  mySoundA.save(f"Sound{i}{j}.mp3")
             elif j==1:
                  mySound_2=gTTS(text=' From  '+" "+myText,lang=language,slow=False)
                  mySound_2.save(f"Sound{i}{j}.mp3")
             elif j==2:
                  mySound_3=gTTS(text=' To  '+" "+myText,lang=language,slow=False)  
                  mySound_3.save(f"Sound{i}{j}.mp3")
             elif j==3:
                   mySound_4=gTTS(text='  By  '+" "+myText,lang=language,slow=False)
                   mySound_4.save(f"Sound{i}{j}.mp3")   
     for i in range(0,4):
        for j in range(0,4):
          playsound(r'D:\my_python\Time_table\Sound{}{}.mp3'.format(i,j))
# For wednesday     
def Wednesday():
     df=pd.read_excel(r'D:\my_python\Time_table\Wednesday.xlsx')

     for i in range(0,4):
   
         for j in range(0,4):
       
             myText=str(df.iloc[i,j])
             language='en'
             if j==0:
                 mySoundA=gTTS(text='  Today is a Class of  '+" "+myText, lang=language, slow=False)
                 mySoundA.save(f"Sound{i}{j}.mp3")
             elif j==1:
                 mySound_2=gTTS(text=' From  '+" "+myText,lang=language,slow=False)
                 mySound_2.save(f"Sound{i}{j}.mp3")
             elif j==2:
                 mySound_3=gTTS(text=' To  '+" "+myText,lang=language,slow=False)  
                 mySound_3.save(f"Sound{i}{j}.mp3")
             elif j==3:
                 mySound_4=gTTS(text='  By  '+" "+myText,lang=language,slow=False)
                 mySound_4.save(f"Sound{i}{j}.mp3")   
     for i in range(0,4):
         for j in range(0,4):
             playsound(r'D:\my_python\Time_tablen\Sound{}{}.mp3'.format(i,j))
 # For Thursday    
def Thursday():
     df=pd.read_excel(r'D:\my_python\Time_table\Thursday.xlsx')

     for i in range(0,4):
   
        for j in range(0,4):
       
             myText=str(df.iloc[i,j])
             language='en'
             if j==0:
                  mySoundA=gTTS(text='  Today is a Class of  '+" "+myText, lang=language, slow=False)
                  mySoundA.save(f"Sound{i}{j}.mp3")
             elif j==1:
                  mySound_2=gTTS(text=' From  '+" "+myText,lang=language,slow=False)
                  mySound_2.save(f"Sound{i}{j}.mp3")
             elif j==2:
                  mySound_3=gTTS(text=' To  '+" "+myText,lang=language,slow=False)  
                  mySound_3.save(f"Sound{i}{j}.mp3")
             elif j==3:
                   mySound_4=gTTS(text='  By  '+" "+myText,lang=language,slow=False)
                   mySound_4.save(f"Sound{i}{j}.mp3")   
     for i in range(0,4):
        for j in range(0,4):
          playsound(r'D:\my_python\Time_table\Sound{}{}.mp3'.format(i,j))
 #For Friday    
def Friday():
     df=pd.read_excel(r'D:\my_python\Time_table\Friday.xlsx')

     for i in range(0,4):
         for j in range(0,4):
       
             myText=str(df.iloc[i,j])
             language='en'
             if j==0:
                  mySoundA=gTTS(text='  Today is a Class of  '+" "+myText, lang=language, slow=False)
                  mySoundA.save(f"Sound{i}{j}.mp3")
             elif j==1:
                  mySound_2=gTTS(text=' From  '+" "+myText,lang=language,slow=False)
                  mySound_2.save(f"Sound{i}{j}.mp3")
             elif j==2:
                  mySound_3=gTTS(text=' To  '+" "+myText,lang=language,slow=False)  
                  mySound_3.save(f"Sound{i}{j}.mp3")
             elif j==3:
                   mySound_4=gTTS(text='  By  '+" "+myText,lang=language,slow=False)
                   mySound_4.save(f"Sound{i}{j}.mp3")   
         for i in range(0,4):
             for j in range(0,4):
                 playsound(r'D:\my_python\Time_table\Sound{}{}.mp3'.format(i,j))

def main():
     now=datetime.now()
     day_c= now.strftime("%A")
     if day_c=='Monday':
         Monday() 
     elif day_c=='Tuesday':
         Tuesday()
     elif day_c=='Wednesday':
         Wednesday()
     elif day_c=='Thursday':
         Thursday()
     elif day_c=='Friday':
         Friday()
     elif day_c=='Saturday':
           myText='Today is Gate classes from 9 AM to 1 PM'
           language='en'
           mySound=gTTS(text=myText,lang=language,slow=False)
           mySound.save("Sound.mp3")
           playsound(r'D:\my_python\Time_table\Sound.mp3')    
if __name__ == "__main__":
       main()     