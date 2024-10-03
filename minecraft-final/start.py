from direct.showbase.ShowBase import ShowBase


# клас
class Game(ShowBase):
    
 def __init__(self):
     ShowBase.__init__(self)
     # завантажуємо модель

     self.model = loader.loadModel('models/environment')
     # переміщення моделі в рендер, зміна батька
     self.model.reparentTo(render)
     # спробуйте змінити розмір моделі
     self.model.setScale(0.1)
     # спробуйте перемістити модель по всіх осях
     self.model.setPos(-2, 25, -3)
    
Game().run()
