from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from appFriendly import appFriendlyOutput
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
<MyWidget>:
    lbl:lbl
    id: my_widget
    text:'Please Choose Your Audio File to See Its Chords. :)'
    FileChooserIconView:
        id: filechooser
        on_selection: my_widget.selected(filechooser.selection)
    Label:
        id:lbl
        text: root.text
        text_size: self.width, None
        halign:'center'
        valign:'middle'
        height:self.texture_size[1]
''')


class ScrollableLabel(ScrollView):
    text = StringProperty('')


class MyWidget(BoxLayout):
   # def open(self, path, filename):
   #    with open(os.path.join(path, filename[0])) as f:
   #         print (f.read())
    text = StringProperty('')

    def selected(self, filename):
        # label=self.ids['lbl']
        if (filename):
            self.text = 'The Chords for this Audio File are: \n' + \
                appFriendlyOutput(filename[0])
        else:
            pass
        # self.text=s
        #print ("selected: %s" % filename[0])


class MyApp(App):
    title = 'ChordIt'

    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
