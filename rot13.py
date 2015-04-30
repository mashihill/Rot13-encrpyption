import webapp2
import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

# Modified from http://stackoverflow.com/questions/14424500/text-shift-function-in-python
strs='abcdefghijklmnopqrstuvwxyz'  # use a string like this, instead of ord() 
strsU='ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # use a string like this, instead of ord() 
def shifttext(inp):
    data=[]
    for i in inp:  #  iterate over the text not some list
        if i.strip() and i in strs:  # if the char is not a space ""  
            data.append(strs[(strs.index(i) + 13) % 26])    
        elif i.strip() and i in strsU:  # if the char is not a space ""  
            data.append(strsU[(strsU.index(i) + 13) % 26])    
        else:
            data.append(i)  #if space the simply append it to data
    output = ''.join(data)
    return output

form="""
<form method="post">
    <h1>ROT 13</h1>

    <textarea name="text">%(ciphertext)s</textarea>

    <br>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, ciphertext=""):
        self.response.out.write(form % {"ciphertext": ciphertext})

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        user_text = shifttext(user_text)
        print user_text

        self.write_form(user_text)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    #('/thanks', ThanksHandler)
], debug=True)
