from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ParentApp(App):

    def on_parent_event(self, instance, parent):
        if parent:
            print(f"{instance.text} was added to the layout.")
        else:
            print(f"{instance.text} was removed from the layout.")

    def build(self):
        layout = BoxLayout(orientation='vertical')

        label1 = Label(text='Label 1')
        label2 = Label(text='Label 2')

        layout.add_widget(label1)
        layout.add_widget(label2)

        label1.bind(on_parent=self.on_parent_event)
        label2.bind(on_parent=self.on_parent_event)

        return layout


if __name__ == '__main__':
    ParentApp().run()
