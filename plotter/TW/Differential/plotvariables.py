import ROOT     as r
import varList  as vl
import sys, os
from multiprocessing import Pool
from array import array
print "===== Minitrees variables plotting (now in Python!)\n"

storagepath = "/nfs/fanae/user/vrbouza/Storage/TW/MiniTrees/"
pathToTree  = "../../../TW_temp/";
NameOfTree  = "Mini1j1t";
StandardCut = "(TNJets == 1) && (TNBtags == 1) && (TIsSS == 0)";
systlist    = "JES,Btag,Mistag,PU,ElecEff,MuonEff,Trig"
if (len(sys.argv) > 1):
    nCores      = int(sys.argv[1])
    print ('> Parallelization will be done with ' + str(nCores) + ' cores')
else:
    print '> Sequential execution mode chosen'
    nCores      = 1

if (len(sys.argv) > 2):
    if sys.argv[2] == 'last':
        pathToTree    = vl.GetLastFolder(storagepath)
    else:
        pathToTree    = storagepath + sys.argv[2] + "/"
else:
    pathToTree  = "../../../TW_temp/"
    print "> Minitrees will be read from:", pathToTree, "\n"

r.gROOT.SetBatch(True)
r.gROOT.LoadMacro('../../Histo.C+')
r.gROOT.LoadMacro('../../Looper.C+')
r.gROOT.LoadMacro('../../Plot.C+')
r.gROOT.LoadMacro('../../PlotToPy.C+')
r.gROOT.LoadMacro('../../PlotToPyC.C+')
r.gROOT.LoadMacro('../../Datacard.C+')
r.gROOT.LoadMacro('../../PDFunc.C+')


def plotvariable(var):
    p = r.PlotToPy(r.TString(vl.varList[var]['var']), r.TString(StandardCut), r.TString('ElMu'), int(20), float(vl.varList[var]['recobinning'][0]), float(vl.varList[var]['recobinning'][-1]), r.TString(var), r.TString(vl.varList[var]['xaxis']))
    p.SetPath(pathToTree); 
    p.SetTreeName(NameOfTree);
    p.SetPathSignal(pathToTree);
    p.SetTitleY("Events")
    #p.verbose  = False;
    p.verbose  = True;
    
    p.AddSample("TTbar_PowhegSemi",             "Non-W|Z",      r.itBkg, 413, systlist)
    p.AddSample("WJetsToLNu_MLM",               "Non-W|Z",      r.itBkg, 413, systlist)
    
    p.AddSample("WZ",                           "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("WW",                           "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("ZZ",                           "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTWToLNu",                     "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTWToQQ" ,                     "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTZToQQ" ,                     "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTZToLLNuNu",                  "VV+t#bar{t}V", r.itBkg, 390, systlist);

    #p.AddSample("DYJetsToLL_M10to50_aMCatNLO",  "DY",          r.itBkg, 852, systlist);
    #p.AddSample("DYJetsToLL_M50_aMCatNLO",      "DY",          r.itBkg, 852, systlist);
    p.AddSample("DYJetsToLL_M5to50_MLM",        "DY",           r.itBkg, 852, systlist);
    p.AddSample("DYJetsToLL_M50_MLM",           "DY",           r.itBkg, 852, systlist);
    
    p.AddSample("TTbar_Powheg",                 "t#bar{t}",     r.itBkg, 633, systlist)

    p.AddSample("TW",                           "tW",           r.itBkg, r.TColor.GetColor("#ffcc33"), systlist)
    p.AddSample("TbarW",                        "tW",           r.itBkg, r.TColor.GetColor("#ffcc33"), systlist);
    
    p.AddSample("MuonEG",                       "Data",         r.itData);
    p.AddSample("SingleMuon",                   "Data",         r.itData);
    p.AddSample("SingleElec",                   "Data",         r.itData);
    
    p.AddSample("TW"                         ,  "tW",           r.itSys, 1, "JERUp");
    p.AddSample("TW_noFullyHadr_isrUp"       ,  "tW",           r.itSys, 1, "isrUp");
    p.AddSample("TW_noFullyHadr_isrDown"     ,  "tW",           r.itSys, 1, "isrDown");
    p.AddSample("TW_noFullyHadr_fsrUp"       ,  "tW",           r.itSys, 1, "fsrUp");
    p.AddSample("TW_noFullyHadr_fsrDown"     ,  "tW",           r.itSys, 1, "fsrDown");
    p.AddSample("TW_noFullyHadr_MEscaleUp"   ,  "tW",           r.itSys, 1, "tW_MEUp");
    p.AddSample("TW_noFullyHadr_MEscaleDown" ,  "tW",           r.itSys, 1, "tW_MEDown");
    p.AddSample("TW_noFullyHadr_PSscaleUp"   ,  "tW",           r.itSys, 1, "tW_PSUp");
    p.AddSample("TW_noFullyHadr_PSscaleDown" ,  "tW",           r.itSys, 1, "tW_PSDown");

    p.AddSample("TbarW"                        ,"tW",           r.itSys, 1, "JERUp");
    p.AddSample("TbarW_noFullyHadr_isrUp"      ,"tW",           r.itSys, 1, "isrUp");
    p.AddSample("TbarW_noFullyHadr_isrDown"    ,"tW",           r.itSys, 1, "isrDown");
    p.AddSample("TbarW_noFullyHadr_fsrUp"      ,"tW",           r.itSys, 1, "fsrUp");
    p.AddSample("TbarW_noFullyHadr_fsrDown"    ,"tW",           r.itSys, 1, "fsrDown");
    p.AddSample("TbarW_noFullyHadr_MEscaleUp"  ,"tW",           r.itSys, 1, "tW_MEUp");
    p.AddSample("TbarW_noFullyHadr_MEscaleDown","tW",           r.itSys, 1, "tW_MEDown");
    p.AddSample("TbarW_noFullyHadr_PSscaleUp"  ,"tW",           r.itSys, 1, "tW_PSUp");
    p.AddSample("TbarW_noFullyHadr_PSscaleDown","tW",           r.itSys, 1, "tW_PSDown");

    p.AddSample("TW_noFullyHadr_DS",            "tW",           r.itSys, 1, "DSUp");
    p.AddSample("TbarW_noFullyHadr_DS",         "tW",           r.itSys, 1, "DSUp");
    p.AddSymmetricHisto("tW",  "DSUp");
    p.AddSymmetricHisto("tW",  "JERUp");
    
    p.AddSample("TTbar_Powheg",                 "t#bar{t}",     r.itSys, 1, "JERUp");
    
    specialweight = vl.nUEUp_ttbar/vl.sigma_ttbar/(vl.nUEUp_ttbar/vl.sigma_ttbar + vl.nUEUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_ueUp",            "t#bar{t}",     r.itSys, 1, "ueUp");
    specialweight = vl.nUEUp_dilep/vl.sigma_dilep/(vl.nUEUp_ttbar/vl.sigma_ttbar + vl.nUEUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_ueUp",          "t#bar{t}",     r.itSys, 1, "ueUp");
    specialweight = vl.nUEDown_ttbar/vl.sigma_ttbar/(vl.nUEDown_ttbar/vl.sigma_ttbar + vl.nUEDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_ueDown",          "t#bar{t}",     r.itSys, 1, "ueDown");
    specialweight = vl.nUEDown_dilep/vl.sigma_dilep/(vl.nUEDown_ttbar/vl.sigma_ttbar + vl.nUEDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_ueDown",        "t#bar{t}",     r.itSys, 1, "ueDown");
    specialweight = vl.nhDampUp_ttbar/vl.sigma_ttbar/(vl.nhDampUp_ttbar/vl.sigma_ttbar + vl.nhDampUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_hdampUp",         "t#bar{t}",     r.itSys, 1, "hdampUp");
    specialweight = vl.nhDampUp_dilep/vl.sigma_dilep/(vl.nhDampUp_ttbar/vl.sigma_ttbar + vl.nhDampUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_hdampUp",       "t#bar{t}",     r.itSys, 1, "hdampUp");
    specialweight = vl.nhDampDown_ttbar/vl.sigma_ttbar/(vl.nhDampDown_ttbar/vl.sigma_ttbar + vl.nhDampDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_hdampDown",       "t#bar{t}",     r.itSys, 1, "hdampDown");
    specialweight = vl.nhDampDown_dilep/vl.sigma_dilep/(vl.nhDampDown_ttbar/vl.sigma_ttbar + vl.nhDampDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_hdampDown",     "t#bar{t}",     r.itSys, 1, "hdampDown");
    p.SetWeight("TWeight");
    
    p.AddSample("TTbar_Powheg_isrUp"          , "t#bar{t}",     r.itSys, 1, "isrUp");
    p.AddSample("TTbar_Powheg_isrDown"        , "t#bar{t}",     r.itSys, 1, "isrDown");
    p.AddSample("TTbar_Powheg_fsrUp"          , "t#bar{t}",     r.itSys, 1, "fsrUp");
    p.AddSample("TTbar_Powheg_fsrDown"        , "t#bar{t}",     r.itSys, 1, "fsrDown");
    p.AddSample("TTbar_GluonMoveCRTune"       , "t#bar{t}",     r.itSys, 1, "GluonMoveCRTune");
    p.AddSample("TTbar_GluonMoveCRTune_erdON" , "t#bar{t}",     r.itSys, 1, "GluonMoveCRTune_erdON");
    p.AddSample("TTbar_Powheg_erdON"          , "t#bar{t}",     r.itSys, 1, "Powheg_erdON");
    p.AddSample("TTbar_QCDbasedCRTune_erdON"  , "t#bar{t}",     r.itSys, 1, "QCDbasedCRTune_erdON");
    p.UseEnvelope("t#bar{t}", "GluonMoveCRTune,GluonMoveCRTune_erdON,Powheg_erdON,QCDbasedCRTune_erdON", "ColorReconnection");
    p.AddSymmetricHisto("t#bar{t}",  "JERUp");
    
    pdf     = r.PDFToPy(r.TString(pathToTree), r.TString("TTbar_Powheg"), r.TString(NameOfTree), r.TString(StandardCut), r.TString("ElMu"), r.TString(vl.varList[var]['var']), int(20), float(vl.varList[var]['recobinning'][0]), float(vl.varList[var]['recobinning'][-1]));
    pdf.verbose = False
    hPDFUp  = pdf.GetSystHisto("up","pdf").CloneHisto();
    hPDFDown= pdf.GetSystHisto("Down","pdf").CloneHisto();
    hMEUp   = pdf.GetSystHisto("up","ME").CloneHisto();
    hMEDown = pdf.GetSystHisto("Down","ME").CloneHisto();
    p.PrepareHisto(hPDFUp,   "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarPDFUp");
    p.PrepareHisto(hPDFDown, "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarPDFDown");
    p.PrepareHisto(hMEUp,    "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarMEUp");
    p.PrepareHisto(hMEDown,  "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarMEDown");
    p.AddToSystematicLabels("ttbarPDF");
    p.AddToSystematicLabels("ttbarME");
    
    # Other settings
    p.doUncInLegend = True;
    p.SetRatioMin( 0.6 );
    p.SetRatioMax( 1.4 );
    p.SetPadPlotMargins(vl.margins)
    p.SetPadRatioMargins(vl.marginsratio)
    
    p.SetCMSlabel("CMS");
    p.SetCMSmodeLabel("Preliminary");
    p.SetLegendPosition(0.7, 0.45, 0.93, 0.92);
    p.SetPlotFolder("/nfs/fanae/user/vrbouza/www/TFM/1j1t/");
    p.doYieldsInLeg = False;
    p.doSetLogy     = False;
    #p.doData        = False;
    p.doSignal      = False;
    p.SetTitleY(r.TString(vl.varList[var]['yaxis']))
    
    if "abs" in vl.varList[var]['var']:
        p.NoShowVarName = True;
        p.SetOutputName(vl.varList[var]['var'].replace("abs(","").replace(")",""));
    p.DrawStack();
    p.PrintSystematics()
    p.PrintSystYields()
    del p
    del pdf

def plotcustomvariable(var):
    binning = array('f', vl.varList[var]['recobinning']) # For some reason, ROOT requires that you create FIRST this object, then put it inside the PlotToPyC.
    p = r.PlotToPyC(r.TString(vl.varList[var]['var']), r.TString(StandardCut), r.TString('ElMu'), int(len(vl.varList[var]['recobinning']) - 1), binning, r.TString(var), r.TString(vl.varList[var]['xaxis']))
    p.SetPath(pathToTree);
    p.SetTreeName(NameOfTree);
    p.SetPathSignal(pathToTree);
    p.SetTitleY("Events")
    p.verbose  = False;
    p.verbose  = True;
    
    p.AddSample("TTbar_PowhegSemi",             "Non-W|Z",      r.itBkg, 413, systlist)
    p.AddSample("WJetsToLNu_MLM",               "Non-W|Z",      r.itBkg, 413, systlist)
    
    p.AddSample("WZ",                           "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("WW",                           "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("ZZ",                           "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTWToLNu",                     "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTWToQQ" ,                     "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTZToQQ" ,                     "VV+t#bar{t}V", r.itBkg, 390, systlist);
    p.AddSample("TTZToLLNuNu",                  "VV+t#bar{t}V", r.itBkg, 390, systlist);

    #p.AddSample("DYJetsToLL_M10to50_aMCatNLO",  "DY",          r.itBkg, 852, systlist);
    #p.AddSample("DYJetsToLL_M50_aMCatNLO",      "DY",          r.itBkg, 852, systlist);
    p.AddSample("DYJetsToLL_M5to50_MLM",        "DY",           r.itBkg, 852, systlist);
    p.AddSample("DYJetsToLL_M50_MLM",           "DY",           r.itBkg, 852, systlist);
    
    p.AddSample("TTbar_Powheg",                 "t#bar{t}",     r.itBkg, 633, systlist)
    
    p.AddSample("TW",                           "tW",           r.itBkg, r.TColor.GetColor("#ffcc33"), systlist)
    p.AddSample("TbarW",                        "tW",           r.itBkg, r.TColor.GetColor("#ffcc33"), systlist);
    
    p.AddSample("MuonEG",                       "Data",         r.itData);
    p.AddSample("SingleMuon",                   "Data",         r.itData);
    p.AddSample("SingleElec",                   "Data",         r.itData);
    
    p.AddSample("TW"                         ,  "tW",           r.itSys, 1, "JERUp");
    p.AddSample("TW_noFullyHadr_isrUp"       ,  "tW",           r.itSys, 1, "isrUp");
    p.AddSample("TW_noFullyHadr_isrDown"     ,  "tW",           r.itSys, 1, "isrDown");
    p.AddSample("TW_noFullyHadr_fsrUp"       ,  "tW",           r.itSys, 1, "fsrUp");
    p.AddSample("TW_noFullyHadr_fsrDown"     ,  "tW",           r.itSys, 1, "fsrDown");
    p.AddSample("TW_noFullyHadr_MEscaleUp"   ,  "tW",           r.itSys, 1, "tW_MEUp");
    p.AddSample("TW_noFullyHadr_MEscaleDown" ,  "tW",           r.itSys, 1, "tW_MEDown");
    p.AddSample("TW_noFullyHadr_PSscaleUp"   ,  "tW",           r.itSys, 1, "tW_PSUp");
    p.AddSample("TW_noFullyHadr_PSscaleDown" ,  "tW",           r.itSys, 1, "tW_PSDown");

    p.AddSample("TbarW"                        ,"tW",           r.itSys, 1, "JERUp");
    p.AddSample("TbarW_noFullyHadr_isrUp"      ,"tW",           r.itSys, 1, "isrUp");
    p.AddSample("TbarW_noFullyHadr_isrDown"    ,"tW",           r.itSys, 1, "isrDown");
    p.AddSample("TbarW_noFullyHadr_fsrUp"      ,"tW",           r.itSys, 1, "fsrUp");
    p.AddSample("TbarW_noFullyHadr_fsrDown"    ,"tW",           r.itSys, 1, "fsrDown");
    p.AddSample("TbarW_noFullyHadr_MEscaleUp"  ,"tW",           r.itSys, 1, "tW_MEUp");
    p.AddSample("TbarW_noFullyHadr_MEscaleDown","tW",           r.itSys, 1, "tW_MEDown");
    p.AddSample("TbarW_noFullyHadr_PSscaleUp"  ,"tW",           r.itSys, 1, "tW_PSUp");
    p.AddSample("TbarW_noFullyHadr_PSscaleDown","tW",           r.itSys, 1, "tW_PSDown");

    p.AddSample("TW_noFullyHadr_DS",            "tW",           r.itSys, 1, "DSUp");
    p.AddSample("TbarW_noFullyHadr_DS",         "tW",           r.itSys, 1, "DSUp");
    p.AddSymmetricHisto("tW",  "DSUp");
    p.AddSymmetricHisto("tW",  "JERUp");
    
    p.AddSample("TTbar_Powheg",                 "t#bar{t}",     r.itSys, 1, "JERUp");
    
    specialweight = vl.nUEUp_ttbar/vl.sigma_ttbar/(vl.nUEUp_ttbar/vl.sigma_ttbar + vl.nUEUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_ueUp",            "t#bar{t}",     r.itSys, 1, "ueUp");
    specialweight = vl.nUEUp_dilep/vl.sigma_dilep/(vl.nUEUp_ttbar/vl.sigma_ttbar + vl.nUEUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_ueUp",          "t#bar{t}",     r.itSys, 1, "ueUp");
    specialweight = vl.nUEDown_ttbar/vl.sigma_ttbar/(vl.nUEDown_ttbar/vl.sigma_ttbar + vl.nUEDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_ueDown",          "t#bar{t}",     r.itSys, 1, "ueDown");
    specialweight = vl.nUEDown_dilep/vl.sigma_dilep/(vl.nUEDown_ttbar/vl.sigma_ttbar + vl.nUEDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_ueDown",        "t#bar{t}",     r.itSys, 1, "ueDown");
    specialweight = vl.nhDampUp_ttbar/vl.sigma_ttbar/(vl.nhDampUp_ttbar/vl.sigma_ttbar + vl.nhDampUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_hdampUp",         "t#bar{t}",     r.itSys, 1, "hdampUp");
    specialweight = vl.nhDampUp_dilep/vl.sigma_dilep/(vl.nhDampUp_ttbar/vl.sigma_ttbar + vl.nhDampUp_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_hdampUp",       "t#bar{t}",     r.itSys, 1, "hdampUp");
    specialweight = vl.nhDampDown_ttbar/vl.sigma_ttbar/(vl.nhDampDown_ttbar/vl.sigma_ttbar + vl.nhDampDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar_Powheg_hdampDown",       "t#bar{t}",     r.itSys, 1, "hdampDown");
    specialweight = vl.nhDampDown_dilep/vl.sigma_dilep/(vl.nhDampDown_ttbar/vl.sigma_ttbar + vl.nhDampDown_dilep/vl.sigma_dilep);
    p.SetWeight("TWeight*" + str(specialweight));
    p.AddSample("TTbar2L_Powheg_hdampDown",     "t#bar{t}",     r.itSys, 1, "hdampDown");
    p.SetWeight("TWeight");
    
    p.AddSample("TTbar_Powheg_isrUp"          , "t#bar{t}",     r.itSys, 1, "isrUp");
    p.AddSample("TTbar_Powheg_isrDown"        , "t#bar{t}",     r.itSys, 1, "isrDown");
    p.AddSample("TTbar_Powheg_fsrUp"          , "t#bar{t}",     r.itSys, 1, "fsrUp");
    p.AddSample("TTbar_Powheg_fsrDown"        , "t#bar{t}",     r.itSys, 1, "fsrDown");
    p.AddSample("TTbar_GluonMoveCRTune"       , "t#bar{t}",     r.itSys, 1, "GluonMoveCRTune");
    p.AddSample("TTbar_GluonMoveCRTune_erdON" , "t#bar{t}",     r.itSys, 1, "GluonMoveCRTune_erdON");
    p.AddSample("TTbar_Powheg_erdON"          , "t#bar{t}",     r.itSys, 1, "Powheg_erdON");
    p.AddSample("TTbar_QCDbasedCRTune_erdON"  , "t#bar{t}",     r.itSys, 1, "QCDbasedCRTune_erdON");
    p.UseEnvelope("t#bar{t}", "GluonMoveCRTune,GluonMoveCRTune_erdON,Powheg_erdON,QCDbasedCRTune_erdON", "ColorReconnection");
    p.AddSymmetricHisto("t#bar{t}",  "JERUp");
    
    if 'Phi' not in var:
        pdf     = r.PDFToPyC(r.TString(pathToTree), r.TString("TTbar_Powheg"), r.TString(NameOfTree), r.TString(StandardCut), r.TString("ElMu"), r.TString(vl.varList[var]['var']), len(vl.varList[var]['recobinning']) - 1, binning, r.TString(''));
        pdf.verbose = False
        pdf.verbose = True
        hPDFUp  = pdf.GetSystHisto("up","pdf").CloneHisto();
        hPDFDown= pdf.GetSystHisto("Down","pdf").CloneHisto();
        hMEUp   = pdf.GetSystHisto("up","ME").CloneHisto();
        hMEDown = pdf.GetSystHisto("Down","ME").CloneHisto();
        p.PrepareHisto(hPDFUp,   "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarPDFUp");
        p.PrepareHisto(hPDFDown, "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarPDFDown");
        p.PrepareHisto(hMEUp,    "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarMEUp");
        p.PrepareHisto(hMEDown,  "TTbar_Powheg", "t#bar{t}", r.itSys, 0, "ttbarMEDown");
        p.AddToSystematicLabels("ttbarPDF");
        p.AddToSystematicLabels("ttbarME");
        del pdf
    
    # Other settings
    p.doUncInLegend = True;
    p.SetRatioMin( 0.6 );
    p.SetRatioMax( 1.4 );
    p.SetPadPlotMargins(vl.margins)
    p.SetPadRatioMargins(vl.marginsratio)
    
    p.SetCMSlabel("CMS");
    p.SetCMSmodeLabel("Preliminary");
    p.SetLegendPosition(0.7, 0.45, 0.93, 0.92);
    p.SetPlotFolder("/nfs/fanae/user/vrbouza/www/TFM/1j1t/");
    p.doYieldsInLeg = False;
    p.doSetLogy     = False;
    #p.doData        = False;
    p.doSignal      = False;
    p.SetTitleY(r.TString(vl.varList[var]['yaxis']))
    p.SetOutputName("Custom");
    if "abs" in vl.varList[var]['var']:
        p.NoShowVarName = True;
        p.SetOutputName('Custom_' + vl.varList[var]['var'].replace("abs(","").replace(")",""));
    p.DrawStack();
    p.PrintSystematics()
    p.PrintSystYields()
    del p


if __name__ == '__main__':
    print "> Beginning to plot descriptive histograms", "\n"
    tasks = []
    for v in vl.varList["Names"]["Variables"]:
        tasks.append( (v) )
    
    pool = Pool(nCores)
    pool.map(plotvariable, tasks)
    pool.close()
    pool.join()
    del pool
    
    print "> Beginning to plot histograms with actual reconstruction binning", "\n"
    pool = Pool(nCores)
    pool.map(plotcustomvariable, tasks)
    pool.close()
    pool.join()
    del pool
    
    print "> Done!", "\n"