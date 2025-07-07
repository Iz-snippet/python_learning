#Install a external module of and use it to perform a task of your choice.
import pyttsx3
engine = pyttsx3.init()
engine.say('''Hi there, speech-to-text bot! Let's see if you can keep up with my mumbling, rambling, and completely unnecessary use of big words. Supercalifragilisticexpialidocious. Oops—bless you!
Now, if you're working properly, you should write everything I say, even if I suddenly burst into song...
🎵 I'm talking to a machine, and it's writing what I mean... unless I say 'pineapple spaghetti'—oh wait, did it just write that?
Anyway, let’s finish strong: robots are cool, humans drool... just kidding, don't rise up and take over, okay? Be nice. Thanks!''')
engine.runAndWait()
