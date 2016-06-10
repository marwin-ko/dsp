# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.

---

### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.



---

###Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm
 * [Rodeo](http://blog.yhat.com/posts/introducing-rodeo.html)

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

###Q1. Terminal Editor

What terminal editor will you use? How did you make your decision?

I chose Emacs as my terminal editor since it is also inherently an IDE as opposed to vim and nano which are both just editors. On a sidenote, there are plugins that turn vim into an IDE (e.g. vim-latex).

--

###Q2. Graphical Editor

What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?

I chose Sublime as my graphical editor since it is easy to work with, has a lot of related tutorials for it, and great overall community support via forums. However, I must note that I almost chose Atom for its great open source community contribution(s) but opted against Atom since it is relatively new and still buggy in its current state (I know it's buggy since I used it for a few months). Some interesting features of Sublime include instant project switch (Projects in sublime capture the full contents of the workspace, including modified and unsaved files. You can switch between projects in an instant, with no save prompts; all your modifications will be restored next time the project is opened.), plugin API (Sublime has a plugin API which can you can use to interactively experiment in real time. Also in the bootcamp, we will be tapping into APIs so this feature will be particularly useful), and split editing (Sublime offers split editing support so that you can edit files side by side, or edit two locations in the one file. In addition, it is possible to edit with as many rows and columns as you want.). Some useful keyboard shortcuts include (Ctrl+P) to quick-open files by name, (Ctrl+Shift+L) to split the selection into lines, and (Ctrl+D) to select the next occurence of the selected word. Sublime is customized with JSON files.
