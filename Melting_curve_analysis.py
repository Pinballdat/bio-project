import pandas as pd

with open("C:/Users/Admin/Desktop/Khanh_result.txt","r") as hd:
    content = hd.read().strip().split("sá»‘ features  ")
    # print(content)
    GC_count = 0
    features = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    features_0 = {"Number of features":[],"%GC":[],"Nh4":[],"DNAcon":[],"E":[],"KCl":[],"Len":[],"Syrbr":[],"Tmcal":[],"deltaG":[],"deltaH":[],"deltaS":[],"Hesotuongquan":[],"Model":[]}
    
    for c in content:
        info = c.strip().split("\n")
        for f in features:
            if info[0] == str(f):
                for i in range(1, len(info)):
                    if len(info[i].split("\t")) > 1:
                        features_0["Number of features"].append(f)
                        features_0["Hesotuongquan"].append(float(info[i].strip().split("\t")[-2]))
                        features_0["Model"].append(info[i].split("\t")[-1])
                        features_0["%GC"].append("Yes") if info[i].find("%GC") != -1 else features_0["%GC"].append("No")
                        features_0["Nh4"].append("Yes") if info[i].find("NH4") != -1 else features_0["Nh4"].append("No")
                        features_0["DNAcon"].append("Yes") if info[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
                        features_0["E"].append("Yes") if info[i].find("E") != -1 else features_0["E"].append("No")
                        features_0["KCl"].append("Yes") if info[i].find("KCl") != -1 else features_0["KCl"].append("No")
                        features_0["Len"].append("Yes") if info[i].find("Len") != -1 else features_0["Len"].append("No")
                        features_0["Syrbr"].append("Yes") if info[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
                        features_0["Tmcal"].append("Yes") if info[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
                        features_0["deltaG"].append("Yes") if info[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
                        features_0["deltaH"].append("Yes") if info[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
                        features_0["deltaS"].append("Yes") if info[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
    df = pd.DataFrame(features_0)
    print(df.tail())
    df.to_excel("C:/Users/Admin/Desktop/Khank_result.xlsx")
    
    
    
    # for c in content:
    #     if c.split("\n")[0] == "0":
    #         features_0["features"].append(c.split("\n")[0])
    #         features_0["Hesotuongquan"].append(c.split("\n")[1].strip().split("\t")[0])
    #         features_0["Note"].append(c.split("\n")[1].strip().split("\t")[1])
    #         features_0["%GC"].append("Yes") if c.find("%GC") != -1 else features_0["%GC"].append("No")
    #         features_0["Nh4"].append("Yes") if c.find("NH4") != -1 else features_0["Nh4"].append("No")
    #         features_0["DNAcon"].append("Yes") if c.find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #         features_0["E"].append("Yes") if c.find("E") != -1 else features_0["E"].append("No")
    #         features_0["KCl"].append("Yes") if c.find("KCl") != -1 else features_0["KCl"].append("No")
    #         features_0["Len"].append("Yes") if c.find("Len") != -1 else features_0["Len"].append("No")
    #         features_0["Syrbr"].append("Yes") if c.find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #         features_0["Tmcal"].append("Yes") if c.find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #         features_0["deltaG"].append("Yes") if c.find("deltaG") != -1 else features_0["deltaG"].append("No")
    #         features_0["deltaH"].append("Yes") if c.find("deltaH") != -1 else features_0["deltaH"].append("No")
    #         features_0["deltaS"].append("Yes") if c.find("deltaS") != -1 else features_0["deltaS"].append("No")

    #     if c.split("\n")[0] == "1":
    #         info_1 = c.strip().split("\n")
    #         # print(info_1)
    #         for i in range(1, len(info_1)):
    #             if len(info_1[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_1[i].strip().split("\t")[1]) 
    #                 features_0["Note"].append(info_1[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_1[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_1[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_1[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_1[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_1[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_1[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_1[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_1[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_1[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_1[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_1[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
                    
    #     if c.split("\n")[0] == "2":
    #         info_2 = c.strip().split("\n")
    #         # print(info_2)
    #         for i in range(1, len(info_2)):
    #             if len(info_2[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_2[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_2[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_2[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_2[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_2[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_2[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_2[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_2[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_2[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_2[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_2[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_2[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_2[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
            
               
    #     if c.split("\n")[0] == "3":
    #         info_3 = c.strip().split("\n")
    #         # print(info_3)
    #         for i in range(1, len(info_3)):
    #             if len(info_3[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_3[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_3[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_3[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_3[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_3[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_3[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_3[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_3[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_3[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_3[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_3[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_3[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_3[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
            
    #     if c.split("\n")[0] == "4":
    #         info_4 = c.strip().split("\n")
    #         # print(info_4)
    #         for i in range(1, len(info_4)):
    #             if len(info_4[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_4[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_4[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_4[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_4[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_4[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_4[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_4[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_4[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_4[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_4[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_4[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_4[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_4[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
            
    #     if c.split("\n")[0] == "5":
    #         info_5 = c.strip().split("\n")
    #         # print(info_5)
    #         for i in range(1, len(info_3)):
    #             if len(info_5[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_5[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_5[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_5[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_5[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_5[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_5[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_5[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_5[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_5[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_5[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_5[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_5[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_5[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
            
    #     if c.split("\n")[0] == "6":
    #         info_6 = c.strip().split("\n")
    #         # print(info_3)
    #         for i in range(1, len(info_6)):
    #             if len(info_6[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_6[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_6[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_6[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_6[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_6[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_6[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_6[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_6[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_6[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_6[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_6[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_6[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_6[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
    #     if c.split("\n")[0] == "7":
    #         info_7 = c.strip().split("\n")
    #         # print(info_7)
    #         for i in range(1, len(info_7)):
    #             if len(info_7[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_7[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_7[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_7[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_7[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_7[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_7[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_7[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_7[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_7[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_7[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_7[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_7[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_7[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
            
    #     if c.split("\n")[0] == "8":
    #         info_8 = c.strip().split("\n")
    #         # print(info_8)
    #         for i in range(1, len(info_8)):
    #             if len(info_8[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_8[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_8[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_8[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_8[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_8[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_8[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_8[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_8[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_8[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_8[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_8[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_8[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_8[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
        
    #     if c.split("\n")[0] == "9":
    #         info_9 = c.strip().split("\n")
    #         # print(info_9)
    #         for i in range(1, len(info_9)):
    #             if len(info_9[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_9[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_9[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_9[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_9[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_9[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_9[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_9[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_9[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_9[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_9[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_9[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_9[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_9[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
        
    #     if c.split("\n")[0] == "10":
    #         info_10 = c.strip().split("\n")
    #         # print(info_10)
    #         for i in range(1, len(info_10)):
    #             if len(info_10[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_10[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_10[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_10[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_10[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_10[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_10[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_10[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_10[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_10[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_10[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_10[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_10[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_10[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
        
    #     if c.split("\n")[0] == "11":
    #         info_11 = c.strip().split("\n")
    #         # print(info_11)
    #         for i in range(1, len(info_11)):
    #             if len(info_11[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_11[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_11[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_11[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_11[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_11[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_11[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_11[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_11[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_11[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_11[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_11[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_11[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_11[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
        
    #     if c.split("\n")[0] == "12":
    #         info_12 = c.strip().split("\n")
    #         # print(info_12)
    #         for i in range(1, len(info_12)):
    #             if len(info_12[i].split("\t")) > 1:
    #                 features_0["features"].append(c.split("\n")[0])
    #                 features_0["Hesotuongquan"].append(info_12[i].strip().split("\t")[-2]) 
    #                 features_0["Note"].append(info_12[i].split("\t")[-1])
    #                 features_0["%GC"].append("Yes") if info_12[i].find("%GC") != -1 else features_0["%GC"].append("No")
    #                 features_0["Nh4"].append("Yes") if info_12[i].find("NH4") != -1 else features_0["Nh4"].append("No")
    #                 features_0["DNAcon"].append("Yes") if info_12[i].find("DNAcon") != -1 else features_0["DNAcon"].append("No")
    #                 features_0["E"].append("Yes") if info_12[i].find("E") != -1 else features_0["E"].append("No")
    #                 features_0["KCl"].append("Yes") if info_12[i].find("KCl") != -1 else features_0["KCl"].append("No")
    #                 features_0["Len"].append("Yes") if info_12[i].find("Len") != -1 else features_0["Len"].append("No")
    #                 features_0["Syrbr"].append("Yes") if info_12[i].find("Syrbr") != -1 else features_0["Syrbr"].append("No")
    #                 features_0["Tmcal"].append("Yes") if info_12[i].find("Tmcal") != -1 else features_0["Tmcal"].append("No")
    #                 features_0["deltaG"].append("Yes") if info_12[i].find("deltaG") != -1 else features_0["deltaG"].append("No")
    #                 features_0["deltaH"].append("Yes") if info_12[i].find("deltaH") != -1 else features_0["deltaH"].append("No")
    #                 features_0["deltaS"].append("Yes") if info_12[i].find("deltaS") != -1 else features_0["deltaS"].append("No")
        
    # print(features_0)
    
