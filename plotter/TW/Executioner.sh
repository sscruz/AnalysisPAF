# Preliminary definitions of samples and so on

samples=("TW" "TW_noFullyHadr" 
  "TbarW" "TbarW_noFullyHadr" 
  "TTbar_Powheg" "TTbar_PowhegSemi" "TTbar2L_powheg" "DYJetsToLL_M50_aMCatNLO" "DYJetsToLL_M10to50_aMCatNLO" 
  "WJetsToLNu_MLM" "ZZ" "WW" "WZ" "TTWToLNu" "TTZToQQ" "TTZToLLNuNu" "TTWToQQ" "TTGJets" 
  "MuonEG" "SingleElec" "SingleMuon")

samples_syst=("TTbar_Powheg_ueUp" "TTbar_Powheg_ueDown" "TTbar_Powheg_isrUp" "TTbar_Powheg_isrDown" "TTbar_Powheg_fsrUp" "TTbar_Powheg_fsrDown" 
  "TTbar_Powheg_hdampUp" "TTbar_Powheg_hdampDown" "TTbar_Powheg_erdON" 
  "TTbar_QCDbasedCRTune_erdON" "TTbar_GluonMoveCRTune" "TTbar_GluonMoveCRTune_erdON" 
  "TW_noFullyHadr_isrUp" "TW_noFullyHadr_isrDown" "TW_noFullyHadr_fsrUp" "TW_noFullyHadr_fsrDown" "TW_noFullyHadr_MEscaleUp" "TW_noFullyHadr_MEscaleDown" 
  "TW_noFullyHadr_PSscaleUp" "TW_noFullyHadr_PSscaleDown" "TW_noFullyHadr_DS" 
  "TbarW_noFullyHadr_isrUp" "TbarW_noFullyHadr_isrDown" "TbarW_noFullyHadr_fsrUp" "TbarW_noFullyHadr_fsrDown" "TbarW_noFullyHadr_MEscaleUp" "TbarW_noFullyHadr_MEscaleDown" 
  "TbarW_noFullyHadr_PSscaleUp" "TbarW_noFullyHadr_PSscaleDown" "TbarW_noFullyHadr_DS")

samples_unf=("UNF_TW" "UNF_TW_noFullyHadr_isrUp" "UNF_TW_noFullyHadr_isrDown" "UNF_TW_noFullyHadr_fsrUp" "UNF_TW_noFullyHadr_fsrDown" "UNF_TW_noFullyHadr_MEscaleUp" "UNF_TW_noFullyHadr_MEscaleDown" 
  "UNF_TW_noFullyHadr_PSscaleUp" "UNF_TW_noFullyHadr_PSscaleDown" "UNF_TW_noFullyHadr_DS" 
  "UNF_TbarW" "UNF_TbarW_noFullyHadr_isrUp" "UNF_TbarW_noFullyHadr_isrDown" "UNF_TbarW_noFullyHadr_fsrUp" "UNF_TbarW_noFullyHadr_fsrDown" "UNF_TbarW_noFullyHadr_MEscaleUp" "UNF_TbarW_noFullyHadr_MEscaleDown" 
  "UNF_TbarW_noFullyHadr_PSscaleUp" "UNF_TbarW_noFullyHadr_PSscaleDown" "UNF_TbarW_noFullyHadr_DS")

runsamples=("TW_ext" "TW_noFullyHadr & TW_noFullyHadr_ext & TW_noFullyHadr_ext2" 
  "TbarW_ext" "TbarW_noFullyHadr & TbarW_noFullyHadr_ext & TbarW_noFullyHadr_ext2" 
  "TTbar_Powheg" "TTbar_Powheg" "TTbar2L_powheg" "DYJetsToLL_M50_aMCatNLO" "DYJetsToLL_M10to50_aMCatNLO & DYJetsToLL_M10to50_aMCatNLO_ext" 
  "WJetsToLNu_MLM & WJetsToLNu_MLM_ext2" "ZZ & ZZ_ext" "WW & WW_ext" "WZ & WZ_ext" "TTWToLNu_ext1 & TTWToLNu_ext2" "TTZToQQ" "TTZToLLNuNu_ext1 & TTZToLLNuNu_ext2" "TTWToQQ" "TTGJets" 
  "MuonEG" "SingleElec" "SingleMuon")

#   runsamples_syst=("TTbar_Powheg_ueUp" "TTbar_Powheg_ueDown" "TTbar_Powheg_isrUp_ext" "TTbar_Powheg_isrDown" "TTbar_Powheg_fsrUp" "TTbar_Powheg_fsrDown" 
#     "TTbar_Powheg_Herwig_ext2" "TTJets_aMCatNLO" "TTbar_Powheg_hdampUp & TTbar_Powheg_hdampUp_ext" "TTbar_Powheg_hdampDown & TTbar_Powheg_hdampDown_ext" "TW_DS" "TbarW_DS" 
#     "TW_noFullyHadr_isrUp" "TW_noFullyHadr_isrDown" "TW_noFullyHadr_fsrUp" "TW_noFullyHadr_fsrDown" "TW_noFullyHadr_MEscaleUp" "TW_noFullyHadr_MEscaleDown" "TbarW_noFullyHadr_isrUp" 
#     "TbarW_noFullyHadr_isrDown" "TbarW_noFullyHadr_fsrUp" "TbarW_noFullyHadr_fsrDown" "TbarW_noFullyHadr_MEscaleUp" "TbarW_noFullyHadr_MEscaleDown" 
#     "TTbar_Powheg_mtop1665" "TTbar_Powheg_mtop1695_backup & TTbar_Powheg_mtop1695_ext & TTbar_Powheg_mtop1695_ext2" "TTbar_Powheg_mtop1735" 
#     "TTbar_Powheg_mtop1755 & TTbar_Powheg_mtop1755_ext & TTbar_Powheg_mtop1755_ext2" "TTbar_Powheg_mtop1785" "TTbar_Powheg_erdON & TTbar_Powheg_erdON_ext" 
#     "TTbar_QCDbasedCRTune_erdON & TTbar_QCDbasedCRTune_erdON_ext" "TTbar_GluonMoveCRTune" "TTbar_GluonMoveCRTune_erdON" "TW_noFullyHadr_mtop1695" "TW_noFullyHadr_mtop1755" 
#     "TbarW_noFullyHadr_mtop1695" "TbarW_noFullyHadr_mtop1755" "TW_noFullyHadr_herwigpp" "TbarW_noFullyHadr_herwigpp")
runsamples_syst=("TTbar_Powheg_ueUp" "TTbar_Powheg_ueDown" "TTbar_Powheg_isrUp_ext" "TTbar_Powheg_isrDown" "TTbar_Powheg_fsrUp" "TTbar_Powheg_fsrDown" 
  "TTbar_Powheg_hdampUp & TTbar_Powheg_hdampUp_ext" "TTbar_Powheg_hdampDown & TTbar_Powheg_hdampDown_ext" "TTbar_Powheg_erdON & TTbar_Powheg_erdON_ext" 
  "TTbar_QCDbasedCRTune_erdON & TTbar_QCDbasedCRTune_erdON_ext" "TTbar_GluonMoveCRTune" "TTbar_GluonMoveCRTune_erdON" 
  "TW_noFullyHadr_isrUp" "TW_noFullyHadr_isrDown" "TW_noFullyHadr_fsrUp" "TW_noFullyHadr_fsrDown" "TW_noFullyHadr_MEscaleUp" "TW_noFullyHadr_MEscaleDown" 
  "TW_noFullyHadr_PSscaleUp" "TW_noFullyHadr_PSscaleDown" "TW_noFullyHadr_DS" 
  "TbarW_noFullyHadr_isrUp" "TbarW_noFullyHadr_isrDown" "TbarW_noFullyHadr_fsrUp" "TbarW_noFullyHadr_fsrDown" "TbarW_noFullyHadr_MEscaleUp" "TbarW_noFullyHadr_MEscaleDown" 
  "TbarW_noFullyHadr_PSscaleUp" "TbarW_noFullyHadr_PSscaleDown" "TbarW_noFullyHadr_DS")

runsamples_unf=("TW_ext" "TW_noFullyHadr_isrUp" "TW_noFullyHadr_isrDown" "TW_noFullyHadr_fsrUp" "TW_noFullyHadr_fsrDown" "TW_noFullyHadr_MEscaleUp" "TW_noFullyHadr_MEscaleDown" 
  "TW_noFullyHadr_PSscaleUp" "TW_noFullyHadr_PSscaleDown" "TW_noFullyHadr_DS" 
  "TbarW_ext" "TbarW_noFullyHadr_isrUp" "TbarW_noFullyHadr_isrDown" "TbarW_noFullyHadr_fsrUp" "TbarW_noFullyHadr_fsrDown" "TbarW_noFullyHadr_MEscaleUp" "TbarW_noFullyHadr_MEscaleDown" 
  "TbarW_noFullyHadr_PSscaleUp" "TbarW_noFullyHadr_PSscaleDown" "TbarW_noFullyHadr_DS")


uplimit=$((${#runsamples[@]}-1))
uplimit_syst=$((${#runsamples_syst[@]}-1))
uplimit_unf=$((${#runsamples_unf[@]}-1))

ncores=("30" "30" 
  "30" "30" 
  "30" "30" "30" "30" "30"
  "8" "8" "8" "8" "8" "8" "8" "8" "5" 
  "30" "30" "30")

unfpath="LocalFile:/pool/ciencias/userstorage/sscruz/TW/mar27/"
unftmppath=""
init="Tree_"
final=".root"
plotspath="/nfs/fanae/user/vrbouza/Documents/TFM/AnalysisPAF/TW_temp"
if [ "$4" != "" ]; then
  plotspath=$4
fi
sel="TW"

if [ "$3" != "" ]; then
  sel=$3
fi
slash="/"
allok=0 
path=""
checker=0
actualsize=0

# Minimum size (in bytes!):
minimumsize=50000

workingpath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


if [ "$1" == "an" ]; then
  echo ""
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% TW ANALYSIS EXECUTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
  echo ""
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Setting up the environment"
  source pre_start.sh

  echo "%%%%%> DONE"
  echo ""
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Starting analysis"
  
  cd ../..
  
  
  if [ "$2" == "opt" ]; then
    echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Running general-purpose samples..."
    for ((i=0; i<=$uplimit; i++)); do
      if [ ${samples[i]} == "TTbar2L_powheg" ]; then
        root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", ${ncores[i]}, -4, 0, 1.0, \"makeHadd\")"
      elif [ ${samples[i]} == "TTbar_PowhegSemi" ]; then
        root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", ${ncores[i]}, 0, 0, 1.0, \"Semi\")"
      else
        root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", ${ncores[i]})"
      fi
      resetpaf -a
    done
    
    echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Running samples for systematic uncertanties..."
    for ((i=0; i<=$uplimit_syst; i++)); do
      root -l -b -q "RunAnalyserPAF.C(\"${runsamples_syst[i]}\", \"$sel\", 20)"
      resetpaf -a
    done
    
    echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Running samples for unfolding procedures..."
    for ((i=0; i<=$uplimit_unf; i++)); do
      unset unftmppath
      unftmppath=$unfpath${runsamples_unf[i]}$final
      root -l -b -q "RunAnalyserPAF.C(\"$unftmppath\", \"$sel\", 30, 0, 0, 35.85, \"Unfolding\")"
      resetpaf -a
    done
    
  else
    echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Running general-purpose samples..."
    for ((i=0; i<=$uplimit; i++)); do
      if [ ${samples[i]} == "TTbar2L_powheg" ]; then
        root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2, -4, 0, 1.0, \"makeHadd\")"
      elif [ ${samples[i]} == "TTbar_PowhegSemi" ]; then
        root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2, 0, 0, 1.0, \"Semi\")"
      else
        root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2)"
      fi
      resetpaf -a
    done
    
    echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Running samples for systematic uncertanties..."
    for ((i=0; i<=$uplimit_syst; i++)); do
      root -l -b -q "RunAnalyserPAF.C(\"${runsamples_syst[i]}\", \"$sel\", $2)"
      resetpaf -a
    done
    
    echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Running samples for unfolding procedures..."
    for ((i=0; i<=$uplimit_unf; i++)); do
      unset unftmppath
      unftmppath=$unfpath${runsamples_unf[i]}$final
      root -l -b -q "RunAnalyserPAF.C(\"$unftmppath\", \"$sel\", $2, 0, 0, 35.85, \"Unfolding\")"
      resetpaf -a
    done
    
  fi
  
elif [ "$1" == "pl" ]; then
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% TW PLOTTER EXECUTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
  echo ""
  echo ""
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Remaking libraries..."  
  source RemakeLibraries.sh
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Starting to plot"
  source PlotThings.sh
  
elif [ "$1" == "ch" ]; then
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% TW CHECKER EXECUTION %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
  echo ""
  echo ""
  echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Remaking libraries..."  
  source pre_start.sh
  echo "%%%%%> DONE"
  echo " "
  
  cd ../..
  
  echo "Checking that the respective..."
  echo $uplimit
  echo "...root files of samples..."
  echo $uplimit_syst
  echo "...root files of systematic samples and..."
  echo $uplimit_unf
  echo "...root files for unfolding procedures exist in..."
  echo $plotspath
  echo "...with selection..."
  echo $sel
  echo "...with at least..."
  echo $minimumsize
  echo "...bytes of size. If they do not fulfil these requirements, they will be reanalysed with..."
  echo $2
  echo "...cores."
  echo " "

  echo "%%%%%%%%> Checking general-purpose samples..."
  while [ $allok != ${#samples[@]} ]; do
    checker=$(($checker+1))
    allok=0
    for ((i=0; i<=$uplimit; i++)); do
      unset path
      unset actualsize
      
      path=$plotspath$slash$init${samples[i]}$final
      
      if [ ! -e $path ]; then
        echo " "
        echo "%%%% => ROOT file not found. The sample that is missing is:"
        echo ${samples[i]}
        echo "Reanalysing..."
        echo " "
        if [ ${samples[i]} == "TTbar2L_powheg" ]; then
          root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2, -4, 0, 1.0, \"makeHadd\")"
        elif [ ${samples[i]} == "TTbar_PowhegSemi" ]; then
          root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2, 0, 0, 1.0, \"Semi\")"
        else
          root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2)"
        fi
        resetpaf -a
        
        allok=$(($allok-8))
      fi
      
      if [ -e $path ]; then
        actualsize=$(wc -c <"$path")
        if [ $actualsize -le $minimumsize ]; then
          echo " "
          echo "%%%% => ROOT file with..."
          echo $actualsize
          echo "...bytes of size, which are lower than the minimum. This sample is:"
          echo ${samples[i]}
          echo "Reanalysing..."
          echo " "
          if [ ${samples[i]} == "TTbar2L_powheg" ]; then
            root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2, -4, 0, 1.0, \"makeHadd\")"
          elif [ ${samples[i]} == "TTbar_PowhegSemi" ]; then
            root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2, 0, 0, 1.0, \"Semi\")"
          else
            root -l -b -q "RunAnalyserPAF.C(\"${runsamples[i]}\", \"$sel\", $2)"
          fi
          resetpaf -a
          
          allok=$(($allok-8))
        fi
      fi
      
      allok=$(($allok+1))
    done
    
    if [ $checker == 10 ]; then
      echo " "
      echo "%%%% => ERROR: limit of iterations (10) reached. There has been a problem with the execution or the general-purpose sample files."
      echo "%%%% => The bash script will now end."
      echo " "
      cd plotter/TW
      exit
    fi
    sleep 5
  done

  path=""
  checker=0
  actualsize=0
  
  echo "%%%%%%%%> Checking samples for systematic uncertanties..."
  while [ $allok != ${#samples_syst[@]} ]; do
    checker=$(($checker+1))
    allok=0
    for ((i=0; i<=$uplimit_syst; i++)); do
      unset path
      unset actualsize
      
      path=$plotspath$slash$init${samples_syst[i]}$final
      
      if [ ! -e $path ]; then
        echo " "
        echo "%%%% => ROOT file not found. The sample that is missing is:"
        echo ${samples_syst[i]}
        echo "Reanalysing..."
        echo " "
        root -l -b -q "RunAnalyserPAF.C(\"${runsamples_syst[i]}\", \"$sel\", $2)"
        resetpaf -a
        
        allok=$(($allok-8))
      fi
      
      if [ -e $path ]; then
        actualsize=$(wc -c <"$path")
        if [ $actualsize -le $minimumsize ]; then
          echo " "
          echo "%%%% => ROOT file with..."
          echo $actualsize
          echo "...bytes of size, which are lower than the minimum. This sample is:"
          echo ${samples_syst[i]}
          echo "Reanalysing..."
          echo " "
          root -l -b -q "RunAnalyserPAF.C(\"${runsamples_syst[i]}\", \"$sel\", $2)"
          resetpaf -a
          
          allok=$(($allok-8))
        fi
      fi
      
      allok=$(($allok+1))
    done
    if [ $checker == 10 ]; then
      echo " "
      echo "%%%% => ERROR: limit of iterations (10) reached. There has been a problem with the execution or the sample files for systematic uncertanties."
      echo "%%%% => The bash script will now end."
      echo " "
      cd plotter/TW
      exit
    fi
    sleep 5
  done
  
  
  path=""
  checker=0
  actualsize=0
  
  echo "%%%%%%%%> Checking samples for unfolding procedures..."
  while [ $allok != ${#samples_unf[@]} ]; do
    checker=$(($checker+1))
    allok=0
    for ((i=0; i<=$uplimit_unf; i++)); do
      unset path
      unset actualsize
      unset unftmppath
      unftmppath=$unfpath${runsamples_unf[i]}$final
      
      path=$plotspath$slash$init${samples_unf[i]}$final
      
      if [ ! -e $path ]; then
        echo " "
        echo "%%%% => ROOT file not found. The sample that is missing is:"
        echo ${samples_unf[i]}
        echo "Reanalysing..."
        echo " "
        root -l -b -q "RunAnalyserPAF.C(\"$unftmppath\", \"$sel\", $2, 0, 0, 35.85, \"Unfolding\")"
        resetpaf -a
        
        allok=$(($allok-8))
      fi
      
      if [ -e $path ]; then
        actualsize=$(wc -c <"$path")
        if [ $actualsize -le $minimumsize ]; then
          echo " "
          echo "%%%% => ROOT file with..."
          echo $actualsize
          echo "...bytes of size, which are lower than the minimum. This sample is:"
          echo ${samples_unf[i]}
          echo "Reanalysing..."
          echo " "
          root -l -b -q "RunAnalyserPAF.C(\"$unftmppath\", \"$sel\", $2, 0, 0, 35.85, \"Unfolding\")"
          resetpaf -a
          
          allok=$(($allok-8))
        fi
      fi
      
      allok=$(($allok+1))
    done
    if [ $checker == 10 ]; then
      echo " "
      echo "%%%% => ERROR: limit of iterations (10) reached. There has been a problem with the execution or the sample files for unfolding procedures."
      echo "%%%% => The bash script will now end."
      echo " "
      cd plotter/TW
      exit
    fi
    sleep 5
  done


  echo "%%%% => All expected ROOT files are in the folder"
  
else
    echo "ERROR - No valid arguments given"
    echo "Please, execute this script with a valid argument"
fi

cd plotter/TW
