#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:37:30 2020

@author: Joe Yapzor
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from UI import ui
from UI.about import Ui_Dialog as About
from UI.help_dialog import Ui_Dialog as Help

from PyQt5.QtGui import *


import numpy as np
import scipy.linalg as LA

class MatrixCalc(ui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MatrixCalc, self).__init__()
        self.ui = ui.Ui_MainWindow()
        self.setupUi(self)
        self.show() 
        
        
        self.x_val.setValidator(QIntValidator())
        self.saveBtn.clicked.connect(lambda:self.save_func())
        self.actionOpen.triggered.connect(lambda: self.open_func())
        self.openBtn.clicked.connect(lambda: self.open_func())
        self.aboutBtn.clicked.connect(lambda: self.about_func())
        self.manualBtn.clicked.connect(lambda: self.manual_func())
        
        self.btn_connect()
        #self.matA.clicked.connect(self.matA_func)
        
    
    
        
    def btn_connect(self):
        
        self.swapBtn.clicked.connect(lambda: self.swapMat())
        
        self.matA.clicked.connect(lambda:self.displayMat(self.matA_func()))
        self.matB.clicked.connect(lambda:self.displayMat(self.matB_func()))
        
        self.invA.clicked.connect(lambda:self.displayMat(self.invA_func()))
        self.invB.clicked.connect(lambda:self.displayMat(self.invB_func()))
        
        self.transA.clicked.connect(lambda:self.displayMat(self.transA_func()))
        self.transB.clicked.connect(lambda:self.displayMat(self.transB_func()))
        
        self.maxA.clicked.connect(lambda:self.displayMat(self.maxA_func()))
        self.maxB.clicked.connect(lambda:self.displayMat(self.maxB_func()))
        
        self.minA.clicked.connect(lambda:self.displayMat(self.minA_func()))
        self.minB.clicked.connect(lambda:self.displayMat(self.minB_func()))
        
        self.normA.clicked.connect(lambda:self.displayMat(self.normA_func()))
        self.normB.clicked.connect(lambda:self.displayMat(self.normB_func()))
        
        self.dimA.clicked.connect(lambda:self.displayMat(self.dimA_func()))
        self.dimB.clicked.connect(lambda:self.displayMat(self.dimB_func()))
        
        self.detA.clicked.connect(lambda: self.displayMat(self.detA_func()))
        self.detB.clicked.connect(lambda: self. displayMat(self.detB_func()))
        
        self.traceA.clicked.connect(lambda: self.displayMat(self.traceA_func()))
        self.traceB.clicked.connect(lambda: self. displayMat(self.traceB_func()))
        self.rankA.clicked.connect(lambda: self.displayMat(self.rankA_func()))
        self.rankB.clicked.connect(lambda: self. displayMat(self.rankB_func()))
        
        self.eigA.clicked.connect(lambda: self.displayMat(self.eigA_func()))
        self.eigB.clicked.connect(lambda: self. displayMat(self.eigB_func()))
        
        self.qrA.clicked.connect(lambda: self.displayMat(self.qrA_func()))
        self.qrB.clicked.connect(lambda: self. displayMat(self.qrB_func()))
        
        self.luA.clicked.connect(lambda: self.displayMat(self.luA_func()))
        self.luB.clicked.connect(lambda: self. displayMat(self.luB_func()))
        
        self.cholA.clicked.connect(lambda: self.displayMat(self.cholA_func()))
        self.cholB.clicked.connect(lambda: self. displayMat(self.cholB_func()))
        
        self.svdA.clicked.connect(lambda: self.displayMat(self.svdA_func()))
        self.svdB.clicked.connect(lambda: self. displayMat(self.svdB_func())) 
        
        
        #######################################################################
        self.addMatAB.clicked.connect(lambda: self.displayMat(self.addmat_func()))
        self.subMatAB.clicked.connect(lambda: self.displayMat(self.submat_func()))
        
        self.arrMulAB.clicked.connect(lambda: self.displayMat(self.arrMulmat_func()))
        self.proAB.clicked.connect(lambda: self.displayMat(self.promat_func()))
        
        self.arrdivmatAB.clicked.connect(lambda: self.displayMat(self.arrDivmat()))
        self.divmatAB.clicked.connect(lambda: self.displayMat(self.Divmat()))
        
        self.logicalAND.clicked.connect(lambda: self.displayMat(self.logicalAND_func()))
        self.logicalOR.clicked.connect(lambda: self.displayMat(self.logicalOR_func()))
        self.logicalXOR.clicked.connect(lambda: self.displayMat(self.logicalXOR_func()))
        
        self.matAmulx.clicked.connect(lambda: self.displayMat(self.matAmulx_func()))
        self.matBmulx.clicked.connect(lambda: self.displayMat(self.matBmulx_func()))
        
        self.matApowx.clicked.connect(lambda: self.displayMat(self.matApowx_func()))
        self.matBpowx.clicked.connect(lambda: self.displayMat(self.matBpowx_func()))


        self.allA.clicked.connect(lambda: self.displayMat(self.allA_func()))
        self.allB.clicked.connect(lambda: self.displayMat(self.allB_func()))
        self.allAB.clicked.connect(lambda: self.displayMat(self.allAB_func()))
        self.autoBtn.clicked.connect(lambda: self.displayMat(self.auto_func()))


    #################FILE FUNCTIONS=========================================
    def save_func(self):
        A= self.generateMatA()
        B = self.generateMatB()
        fname = QFileDialog.getSaveFileName(self, 'BJ Matrix Calc - Save Matrix Data', '',('*.npy'))
        fname = fname[0]
        np.save(fname,[A, B])
    
    def open_func(self):
        fname = QFileDialog.getOpenFileName(self, 'BJ Matrix Calc - Open Matrix Data', '', ('*.npy'))[0]
        A= np.load(fname)[0]
        B= np.load(fname)[1]
        A= str(A).replace(']', ''); A= str(A).replace('[', '')
        B= str(B).replace(']', ''); B= str(B).replace('[', '')
        self.matAEntry.clear(), self.matAEntry.insertPlainText(str(A))
        self.matBEntry.clear(), self.matBEntry.insertPlainText(B)
    
    def about_func(self):
        dialog = QDialog()
        dialog.ui= About()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()
    
    def manual_func(self):
        dialog = QDialog()
        dialog.ui= Help()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()
    
    
    def displayMat(self, mat):
        A= str(mat).replace(']', '')
        mat= str(A).replace('[', '')
        self.resultsEntry.appendPlainText(str(mat))
        self.resultsEntry.appendPlainText('\n')
    
    def swapMat(self):
        matA= self.matAEntry.toPlainText()
        matB= self.matBEntry.toPlainText()
        
        self.matAEntry.clear()
        self.matAEntry.appendPlainText(matB)
        self.matBEntry.clear()
        self.matBEntry.appendPlainText(matA)
        
    def generateMatA(self):
        matA= self.matAEntry.toPlainText()
        precisionVal = int(self.precisionVal.currentText())
        np.set_printoptions(precision=precisionVal)
        f=open('matA.txt', 'w'); f.write(matA); f.close()
        try:
            A=np.genfromtxt('matA.txt', delimiter=' ')
            return A
        except ValueError:
            return   'Rows or Columns of Matrix A do not Match'
    
    def generateMatB(self):
        matB= self.matBEntry.toPlainText()
        precisionVal = int(self.precisionVal.currentText())
        np.set_printoptions(precision=precisionVal)
        f=open('matB.txt', 'w'); f.write(matB); f.close()
        try:
            B=np.genfromtxt('matB.txt', delimiter=' ')
            return B
        except ValueError:
            return   'Rows or Columns of Matrix B do not Match'

################################################################################################
    ############### MATRIX FUNCTIONS================================================
    def matA_func(self):
                
        A=self.generateMatA()
        A= f'''Matrix A=
{A}'''
        return str(A)
            

    def matB_func(self):
        B=self.generateMatB()
        B= f'''Matrix B= \n{B}'''
        return str(B)
    
    def invA_func(self):
        A= self.generateMatA()
        
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                invA = np.linalg.inv(A)
                invA = f'''Inverse of Matrix A=\n {invA}'''
                return invA
            except Exception as err:
                return f'''Inverse of Matrix A \n{err}'''
    
    def invB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                invB = np.linalg.inv(B)
                invB= f'''Inverse of Matrix B=\n{invB}'''
                return invB
            except Exception as err:
                return f'''Inverse of Matrix B\n{err}'''
    
    def transA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try: 
                transA = A.T
                transA= f'''Transpose of Matrix A=\n{transA}'''
                return transA
            except Exception as err:
                return f'''Transpose of Matrix A\n{err}'''
    
    def transB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                transB = B.T 
                transB =f'''Transpose of Matrix B=\n{transB}'''
                return transB
            except Exception as err:
                return f'''Inverse of Matrix B\n{err}'''
    
    def maxA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                maxA = A.max()
                precisionVal = int(self.precisionVal.currentText())
                maxA = round(maxA, precisionVal)
                maxA = f'''Maximum Element of Matrix A=\n\t{maxA}'''
                return maxA
            except Exception as err:
                return f'''Maximum of Matrix A\n{err}'''
    
    def maxB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                maxB = B.max()
                maxB= round(maxB, precisionVal)
                maxB= f'''Maximum Element of Matrix B=\n\t{maxB}'''
                return maxB
            except Exception as err:
                return f'''Maximum of Matrix B\n{err}'''
    
    def minA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                minA = A.min() 
                minA= round(minA, precisionVal)
                minA= f'''Minimum Element of Matrix A=\n\t{minA}'''
                return minA
            except Exception as err:
                return f'''Minimum Element of Matrix A\n{err}'''
    
    def minB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                minB = B.min()
                minB = round(minB, precisionVal)
                minB = f'''Minimum Element of Matrix B=\n\t{minB}'''
                return minB
            except Exception as err:
                return f'''Minimum Element of Matrix B\n{err}'''
    
    def normA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                normA = np.linalg.norm(A) 
                normA = round(normA, precisionVal)
                normA= f'''Norm of Matrix A=\n\t{normA}'''
                return normA
            except Exception as err:
                return f'''Norm of Matrix B\n{err}'''
    
    def normB_func(self):
        B= self.generateMatB()
        precisionVal = int(self.precisionVal.currentText())
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                normB = np.linalg.norm(B) 
                normB= round(normB, precisionVal)
                normB= f'''Norm of Matrix B=\n\t{normB}'''
                return normB
            except Exception as err:
                return f'''Norm of Matrix B\n{err}'''
    
    def dimA_func(self):
        A= self.generateMatA()
        
        dimA = str(np.shape(A)).replace('(', '').replace(')', '').replace(',', ' * ')
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                dimA= f'''Dimensions of Matrix A=\n\t{dimA}'''
                return dimA
            except Exception as err:
                return f'''Dimensions of Matrix A\n{err}'''
    
    def dimB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                dimB = str(np.shape(B)).replace('(', '').replace(')', '').replace(',', ' * ')
                
                dimB= f'''Dimensions of Matrix B=\n\t{dimB}'''
                return dimB
            except Exception as err:
                return f''' Dimensions of Matrix B\n{err}'''
    
    def detA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                detA = np.linalg.det(A)
                detA= round(detA, precisionVal)
                detA =  f'''Determinant of Matrix A=\n\t{detA}'''
                return detA 
            except Exception as err:
                return f'''Determinant of Matrix A\n{err}'''
            
    def detB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                detB= np.linalg.det(B)
                detB= round(detB, precisionVal)
                detB=  f'''Determinant of Matrix B=\n\t{detB}'''
                return detB
            except Exception as err:
                return f'''Determinant of Matrix B\n{err}'''

    def traceA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                traceA = np.trace(A)
                traceA= round(traceA, precisionVal)
                traceA=  f'''Trace of Matrix A=\n\t{traceA}'''
                return traceA 
            except Exception as err:
                return f'''Trace of Matrix A\n{err}'''
    
    def traceB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                precisionVal = int(self.precisionVal.currentText())
                traceB= np.trace(B)
                traceB = round(traceB, precisionVal)
                traceB=  f'''Trace of Matrix B= \n\t{traceB}'''
                return traceB
            except Exception as err:
                return f'''Trace of Matrix B\n{err}'''
    
    def rankA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                rankA = np.linalg.matrix_rank(A)
                rankA =  f'''Rank of Matrix A=\n\t{rankA}'''
                return rankA 
            except Exception as err:
                return f'''Rank of Matrix A\n{err}'''
    
    def rankB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                rankB= np.linalg.matrix_rank(B)
                rankB=  f'''Rank of Matrix B=\n\t{rankB}'''
                return rankB
            except Exception as err:
                return f'''Rank of Matrix B\n{err}'''
        
    def eigA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                eigValA= np.linalg.eigvals(A)
                eigVecA= np.diag(np.linalg.eig(A)[0])
                
                eigA= f'''Eig Values of A, P=:\n{eigValA} \n Eig Vectors of A, D=: \n{eigVecA}'''
                return eigA
            except Exception as err:
                return f'''EigenValues of Matrix A\n{err}'''
    
    def eigB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                eigValB= np.linalg.eigvals(B)
                eigVecB= np.diag(np.linalg.eig(B)[0])
                eigB= f'''Eig Values of B, P=: \n{eigValB} \nEig Vectors of B, D=: \n{eigVecB}'''
                return eigB
            except Exception as err:
                return f'''EigenValues of Matrix B\n{err}'''
    
    def qrA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                qA= np.linalg.qr(A)[0] 
                rA= np.linalg.qr(A)[1]
                
                qrA= f''' Orthogonal Q Matrix of A: \n{qA} \nR = \n{rA} '''
                return qrA
            except Exception as err:
                return f'''QR Factorization of Matrix A\n{err}'''
        
    
    def qrB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                qB= np.linalg.qr(B)[0] 
                rB= np.linalg.qr(B)[1]
                
                qrB= f''' Orthogonal Q Matrix of B: \n{qB} \n R = \n{rB} '''
                return qrB
            except Exception as err:
                return f'''QR Factorization of Matrix B\n{err}'''
        
        
    def luA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                P,L,U= LA.lu(A)
                
                luA= f''' LU Factorization of A, P= \n{P} \n L= \n{L} \n U= \n{U}'''
                return luA
            except Exception as err:
                return f'''LU Factorization of Matrix A\n{err}'''
    
    def luB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                P,L,U= LA.lu(B)
                
                luB= f'''LU factorization of B, P= \n{P} \n L= \n{L} \n U= \n{U}'''
                return luB
            except Exception as err:
                return f'''LU factorization of Matrix B\n{err}'''


    def cholA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                cholA= np.linalg.cholesky(A)
                cholA=  f'''Cholesky Factorization of Matrix B= \n{cholA}'''
                return cholA
            except Exception as err:
                return f'''Cholesky Matrix A \n{err}'''
    
    def cholB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                cholB= np.linalg.cholesky(B)
                cholB= f'''Cholesky Factorization of Matrix B= \n{cholB}'''
                return cholB
            except Exception as err:
                return f'''Cholesky Matrix B \n{err}'''
            
        
    def svdA_func(self):
        A= self.generateMatA()
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                u, s, vh= np.linalg.svd(A) 
                
                svdA = f''' SVD of A, U: \n{u} \n S = \n{s} \n\n V= \n{vh}'''
                return svdA
            except Exception as err:
                return f'''SVD Factorization of Matrix A\n{err}'''

    def svdB_func(self):
        B= self.generateMatB()
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                u, s, vh= np.linalg.svd(B) 
                
                svdB = f'''SVD of B, U: \n{u}  \n S = \n{s}  \n\n V= \n{vh}'''
                return svdB
            except Exception as err:
                return f'''SVD Factorization of Matrix B\n{err}'''
   
    
    def addmat_func(self):
        A= self.generateMatA()
        B=self.generateMatB()
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            if np.shape(A) != np.shape(B):
                return 'Cannot ADD Matrices with Different Dimensions'
            else:
                try:
                    addMat = np.add(A,B)
                    addMat= f''' Matrix A plus Matrix B= \n{addMat}'''
                    return addMat 
                except Exception as err:
                    return f'''Addition of Matrix A and B\n{err}'''
    
    
    def submat_func(self):
        A= self.generateMatA()
        B=self.generateMatB()
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            if np.shape(A) != np.shape(B):
                return 'Cannot SUBTRACT Matrices with Different Dimensions'
            else:
                try:
                    subMat = np.subtract(A, B)
                    subMat = f''' Matrix A minus Matrix B= \n{subMat}'''
                    return subMat 
                except Exception as err:
                    return f'''Subtraction of Matrix A and B\n{err}'''
    
    def arrMulmat_func(self):
        A= self.generateMatA()
        B=self.generateMatB()
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            try:
                mulMat = np.multiply(A, B)
                mulMat= f'''Element-wise Multiplication of  A and B= \n{mulMat}'''
                return mulMat 
            except Exception as err:
                    return f'''Element-wise Multiplication of Matrix A and B\n{err}'''
                
                
    def promat_func(self):
        A= self.generateMatA()
        B=self.generateMatB()
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            try:
                mulMat = np.matmul(A, B)
                mulMat= f'''Matrix Product of Matrix A and B= \n{mulMat}'''
                return mulMat 
            except Exception as err:
                return f'''Product of Matrix A and B\n{err}'''
    
    def arrDivmat(self):
        A= self.generateMatA()
        B=self.generateMatB() 
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            try:
                divMat = A/B 
                divMat= f'''Element-wise Division of  A and B= \n{divMat}'''
                return divMat 
            except Exception as err:
                return f'''Element-wise Division of Matrix A and B\n{err}'''
    
    def Divmat(self):
        A= self.generateMatA()
        B=self.generateMatB() 
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            try:
                divMat = np.matmul(A, np.linalg.inv(B))
                divMat= f'''Matrix Divisiion of Matrix A and B= \n{divMat}'''
                return divMat 
            except Exception as err:
                return f'''Division of Matrix A and B\n{err}'''
    
    def logicalAND_func(self):
        A= self.generateMatA()
        B= self.generateMatB()
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            try:
                AND = np.logical_and(A,B)
                AND= f'''Element-wise Logical AND of Matrix A and B= \n{AND}'''
                return AND
            except Exception as err:
                return f'''Element-wise Logical AND of Matrix A and B\n{err}'''
    
    def logicalOR_func(self):
        A= self.generateMatA()
        B= self.generateMatB()
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            try:
                OR = np.logical_or(A,B)
                OR =  f'''Element-wise Logical OR of Matrix A and B= \n{OR}'''
                return OR 
            except Exception as err:
                    return f'''Logical OR of Matrix A and B\n{err}'''
    
    def logicalXOR_func(self):
        A= self.generateMatA()
        B= self.generateMatB()
        if B=='Rows or Columns of Matrix B do not Match' or A=='Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A or B do not Match'
        else:
            try:
                XOR = np.logical_xor(A,B)
                XOR=  f'''Exclusive Logical OR / XOR of Matrix A and B= \n{XOR}'''
                return XOR
            except Exception as err:
                    return f'''Exlusive Logical OR[XOR] of Matrix A and B\n{err}'''
    
    
    def matAmulx_func(self):
        A= self.generateMatA()
        x= int(self.x_val.text())
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                matAx= A*x
                matAx=  f'''Matrix A times x= \n{matAx}'''
                return matAx
            except Exception as err:
                    return f'''Matrix A times x \n{err}'''
    
    def matBmulx_func(self):
        B= self.generateMatB()
        x= int(self.x_val.text())
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                matBx= B*x
                matBx =f'''Matrix B times x \n{matBx}'''
                return matBx
            except Exception as err:
                    return f'''Matrix B times x \n{err}'''
   
    def matApowx_func(self):
        A= self.generateMatA()
        x= int(self.x_val.text())
        if A== 'Rows or Columns of Matrix A do not Match':
            return 'Rows or Columns of Matrix A do not Match'
        else:
            try:
                matAx= np.linalg.matrix_power(A, x)
                matAx = f'''Matrix A raised to the power x \n{matAx}'''
                return matAx
            except Exception as err:
                    return f'''Matrix A raised to the power x \n{err}'''
    
    
    def matBpowx_func(self):
        B= self.generateMatB()
        x= int(self.x_val.text())
        if B== 'Rows or Columns of Matrix B do not Match':
            return 'Rows or Columns of Matrix B do not Match'
        else:
            try:
                matBx= np.linalg.matrix_power(B, x)
                matBx= f'''Matrix B raised to the power x \n{matBx}'''
                return matBx
            except Exception as err:
                    return f'''Matrix B raised to the power x \n{err}'''
    
    def allA_func(self):
        self.displayMat(self.matA_func())
        self.displayMat(self.invA_func())
        self.displayMat(self.transA_func())
        self.displayMat(self.maxA_func())
        self.displayMat(self.minA_func())
        self.displayMat(self.normA_func())
        self.displayMat(self.dimA_func())
        self.displayMat(self.detA_func())
        self.displayMat(self.traceA_func())
        self.displayMat(self.rankA_func())
        self.displayMat(self.eigA_func())
        self.displayMat(self.qrA_func())
        self.displayMat(self.luA_func())
        self.displayMat(self.cholA_func())
        self.displayMat(self.svdA_func())


    
    def allB_func(self):
        self.displayMat(self.matB_func())
        self.displayMat(self.invB_func())
        self.displayMat(self.transB_func())
        self.displayMat(self.maxB_func())
        self.displayMat(self.minB_func())
        self.displayMat(self.normB_func())
        self.displayMat(self.dimB_func())
        self.displayMat(self.detB_func())
        self.displayMat(self.traceB_func())
        self.displayMat(self.rankB_func())
        self.displayMat(self.eigB_func())
        self.displayMat(self.qrB_func())
        self.displayMat(self.luB_func())
        self.displayMat(self.cholB_func())
        self.displayMat(self.svdB_func())
        self.displayMat(self.matBmulx_func())
        self.displayMat(self.matBpowx_func())

    def allAB_func(self):
        self.displayMat(self.addmat_func())
        self.displayMat(self.submat_func())
        self.displayMat(self.arrMulmat_func())
        self.displayMat(self.promat_func())
        self.displayMat(self.arrDivmat())
        self.displayMat(self.Divmat())
        self.displayMat(self.logicalAND_func())
        self.displayMat(self.logicalOR_func())
        self.displayMat(self.logicalXOR_func())


    def auto_func(self):
        self.displayMat(self.matA_func())
        self.displayMat(self.matB_func())
        self.displayMat(self.invA_func())
        self.displayMat(self.invB_func())
        self.displayMat(self.transA_func())
        self.displayMat(self.transB_func())
        self.displayMat(self.maxA_func())
        self.displayMat(self.maxB_func())
        self.displayMat(self.minA_func())
        self.displayMat(self.minB_func())
        self.displayMat(self.normA_func())
        self.displayMat(self.normB_func())
        self.displayMat(self.dimA_func())
        self.displayMat(self.dimB_func())
        self.displayMat(self.detA_func())
        self.displayMat(self.detB_func())
        self.displayMat(self.traceA_func())
        self.displayMat(self.traceB_func())
        self.displayMat(self.rankA_func())
        self.displayMat(self.rankB_func())
        self.displayMat(self.eigA_func())
        self.displayMat(self.eigB_func())
        self.displayMat(self.qrA_func())
        self.displayMat(self.qrB_func())
        self.displayMat(self.luA_func())
        self.displayMat(self.luB_func())
        self.displayMat(self.cholA_func())
        self.displayMat(self.cholB_func())
        self.displayMat(self.svdA_func())
        self.displayMat(self.svdB_func())
        self.displayMat(self.addmat_func())
        self.displayMat(self.submat_func())
        self.displayMat(self.arrMulmat_func())
        self.displayMat(self.promat_func())
        self.displayMat(self.arrDivmat())
        self.displayMat(self.Divmat())
        self.displayMat(self.logicalAND_func())
        self.displayMat(self.logicalOR_func())
        self.displayMat(self.logicalXOR_func())
        self.displayMat(self.matAmulx_func())
        self.displayMat(self.matBmulx_func())
        self.displayMat(self.matApowx_func())
        self.displayMat(self.matBpowx_func())
        


#######Correct Errors of Unmatching Rows and Columns 
    
    
    

if __name__=='__main__':
    app = QApplication(sys.argv)
    w = MatrixCalc()
    w.show()
    sys.exit(app.exec_())