# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = [0.2, 0.2, 0.2]            
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
                [0,0,0],
                [self.parameters['width'],0,0],
                [self.parameters['width'],0,self.parameters['height']],
                [0,0,self.parameters['height']],
                [0,self.parameters['thickness'],0],
                [self.parameters['width'],self.parameters['thickness'],0],
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],
                [0,self.parameters['thickness'],self.parameters['height']],
                ]
                
    
        self.faces = [
                [0,1,2,3],
                [1,5,6,2],
                [2,3,7,6],
                [5,4,7,6],
                [0,4,7,3],
                [0,1,5,4]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        pass      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):

        def draw(self):

          self.drawEdges()
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotatef(self.parameters['orientation'],0,0,1)

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE) #tracé des faces
        gl.glBegin(gl.GL_QUADS) #tracé d'un parallélépipède par les 8 sommets
        gl.glColor3fv(self.parameters['edges']) #définition de la couleur de chaque face

        for i in self.faces: #parcours de la liste de self.faces
          for j in i:  #j est l'indice des sommets du parallélépipède
            gl.glVertex3fv(self.vertices[j]) #cette commande récupère les coordonées de chaque sections de la liste vertices
        
        gl.glEnd()
        gl.glPopMatrix()           
                    
    # Draws the faces
    def draw(self):

        self.drawEdges()
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotatef(self.parameters['orientation'],0,0,1)

        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_FILL) #tracé des faces
        gl.glBegin(gl.GL_QUADS) #tracé d'un parallélépipède par les 8 sommets
        gl.glColor3fv(self.parameters['color']) #définition de la couleur de chaque face

        for i in self.faces: #parcours de la liste de self.faces
          for j in i:  #j est l'indice des sommets du parallélépipède
            gl.glVertex3fv(self.vertices[j]) #cette commande récupère les coordonées de chaque sections de la liste vertices
        
        gl.glEnd()
        gl.glPopMatrix()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  