#PASO 1. DEFINIR LA CLASE
class Celular:
    #PASO 2. INICIALIZAR EL CONSTRUCTOR - PROPIEDADES
    def __init__(self,camara,pantalla,bateria,botones,entradaCarga,sistemaOperativo,tipoCarga):
        self.camara=camara
        self.pantalla=pantalla
        self.bateria=bateria
        self.botones=botones
        self.entradaCarga=entradaCarga
        self.sistemaOperativo=sistemaOperativo
        self.tipoCarga=tipoCarga
    #PASO 3. DEFINIR LAS ACCIONES
    def llamar(self,numero):
        print("Realizando la llamada ", numero)
    def accederInternet(self,conectividad):
        if conectividad==True:
            print("Accediendo a Internet")
        else: 
            print("No tiene acceso a intenet verifique su conexion...")
    def tomarFoto(self):
        print("Sacando foto... Foto guardada...")
    def verHora(self):
        print("Mostrando la hora...")

#PASO 4. CREACION DE LOS OBJETOS
celular1=Celular("120px","6.5","5000","3","tipo C","Myos","Inhalambrica")
celular2=Celular("48px","6","2000","3","Tipo C","EmuiOs","Alambrica")

celular1.llamar(65402398)
celular2.accederInternet(False)
celular2.llamar(74561235)