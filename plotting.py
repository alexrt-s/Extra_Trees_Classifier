
"""
2021, Alexander Thomson-Strong
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################
This code can be used to plot graphs comparing the processing time and AUC scores
of two paper recommendation models, to evaluate which one is better.
"""
import matplotlib.pyplot as plt
import numpy as np

#path to the files which contains the data being plotted
model1_path = '/path/to/file/model1' 
model2_path = '/path/to/file/model2'


model1_AUC_file = model1_path + "/AUC_vs_data_cmp.dat"
model1_process_file = model1_path + "/process_time_vs_data_cmp.dat"

model2_AUC_file = model2_path + "/AUC_vs_data_cmp.dat"
model2_process_file = model2_path + "/process_time_vs_data_cmp.dat"

#path to the locations that the graphs will be saved to
AUC_save_path = '/path/to/file/AUC_graph_save_location'
process_save_path = '/path/to/file/process_graph_save_location'

#reads in the data from file for model 1
with open(model1_AUC_file,"r") as f:
    model1_AUCS = np.empty(0)
    model1_process = np.empty(0)
    model1_papers = np.empty(0)
    model1_error = np.empty(0)
    model1_user = np.empty(0)
    for line in f:
        if line.startswith("#") is False:
            data = line.split(" ")
            
            model1_user = np.append(model1_user,float(data[0]))
            model1_papers = np.append(model1_papers,float(data[1]))
            model1_AUCS = np.append(model1_AUCS,float(data[2]))
            model1_error = np.append(model1_error,float(data[3]))
            
with open(model1_process_file,"r") as f:
    model1_process = np.empty(0)
    for line in f:
        if line.startswith("#") is False:
            data = line.split(" ")
            model1_process = np.append(model1_process,float(data[2]))
            
#reads in the data from file for model 2           
with open(model2_AUC_file,"r") as f:
    model2_AUCS = np.empty(0)
    model2_process = np.empty(0)
    model2_papers = np.empty(0)
    model2_error = np.empty(0)
    model2_user = np.empty(0)
    for line in f:
        if line.startswith("#") is False:
            data = line.split(" ")
            
            model2_user = np.append(model2_user,float(data[0]))
            model2_papers = np.append(model2_papers,float(data[1]))
            model2_AUCS = np.append(model2_AUCS,float(data[2]))
            model2_error = np.append(model2_error,float(data[3]))
            
with open(model2_process_file,"r") as f:
    model2_process = np.empty(0)
    for line in f:
        if line.startswith("#") is False:
            data = line.split(" ")
            model2_process = np.append(model2_process,float(data[2]))

#produces the AUC plot for both models and saves it to file      
plt.figure()
plt.errorbar(model1_papers,model1_AUCS,yerr = model1_error,elinewidth = 0.5,fmt = 'o',mfc = 'w',ms = 2,mec = 'b')
plt.errorbar(model2_papers,model2_AUCS,yerr=model2_error,elinewidth = 0.5,fmt = 'o',mfc = 'w',ms = 2,mec = 'r')
plt.errorbar(0,0,yerr=0,elinewidth=0)
plt.xlabel('data points/papers')
plt.ylabel('AUC')
plt.xscale('log')
plt.title('AUC as a function of training data for both models')
plt.text(x=1000,y=0.2,s='model 1 mean AUC = '  + str(np.mean(model1_AUCS)))
plt.text(x=1000,y=0.4,s='model 2 mean AUC = ' + str(np.mean(model2_AUCS)))
plt.savefig(AUC_save_path + "/AUC_Curve_(%s,%s,%s).png" % (int(model1_user[0]),int(model1_user[-1]),int(model1_user[1] - model1_user[0])))
plt.clf()

#produces the processing time plot for bith models and saves it to file
plt.figure()
plt.scatter(model1_papers,model1_process,s=0.5)
plt.scatter(model2_papers,model2_process,s=0.5)
plt.xlabel('data points/papers')
plt.ylabel('processing time/seconds')
plt.title('Processing time as a function of training data')
plt.text(x=50,y=500,s='model 1 processing time = ' + str(np.sum(model1_process)) + ' seconds')
plt.text(x=50,y=700,s='model 2 processing time = ' + str(np.sum(model2_process)) + ' seconds')
plt.savefig(process_save_path + '/Processing_time_process_time_(%s,%s,%s).png' % (int(model1_user[0]),int(model1_user[-1]),int(model1_user[1] - model1_user[0])))
plt.clf()
            

           
            
            
            
