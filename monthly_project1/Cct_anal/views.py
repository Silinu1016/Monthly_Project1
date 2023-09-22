from django.shortcuts import render, HttpResponse
from .models import Post_Customer,Post_Cunsumption
# Create your views here.
def index(request):
    return render(request,'Homepage_1.html',{}) 

def participant(request):
    return render(request,'Homepage_2.html',{}) 
    
def data_disc1(request):
    return render(request,'Homepage_3_1.html',{}) 

def data_disc2(request):
    col = [["출생연도","Year_Birth"], ["교육 수준", "Education"], [ "결혼 여부","Marital_Status" ], ["소득" , "Income"], ["자녀(어린이) 여부","Kidhome"], [ "자녀(청소년) 여부","Teenhome" ],  [ "최근 구매일","Recency"] , ["불만 사항","Complain"]]
    col2 = [["와인","MntWines"],[ "과일", "MntFruits"],["고기", "MntMeatProducts"], ["생선","MntFishProducts"], ["과자", "MntSweetProducts"], ["금","MntGoldProds"]]
    return render(request,'Homepage_3_2.html',{"Columns":col,"Columns2":col2}) 

def data_disc3(request):
    return render(request,'Homepage_3_3.html',{}) 

def data_anal1(request):
    return render(request,'Homepage_4_1.html',{}) 

def data_anal2(request):
    return render(request,'Homepage_4_2.html',{}) 

def data_anal3(request):
    return render(request,'Homepage_4_3.html',{}) 

def data_anal4(request):
    return render(request,'Homepage_4_4.html',{}) 

def data_anal5(request):
    C_L = ["Birth",    "Child",    "Educ",    "Inco",    "Marr",    "Rece",    "Teen"]
    Co_L = ["Gold",    "Fruit",    "Meat",    "Fish",    "Snack",    "Wine"]
    C_D = {"Birth":"Birthyear","Child":"Child","Educ":"Education","Inco":"Income","Marr":"Marry","Rece":"Recently","Teen":"Teen"}
    List = []
    if request.method == 'POST':
        selected_Cus = request.POST.getlist('Cus_List')
        selected_Cun = request.POST.getlist('Cun_List')
        if len(selected_Cus)==1 and len(selected_Cun)==1:
            List =  [C_D[selected_Cus[0]]+"_"+selected_Cun[0]]
    return render(request,'Homepage_4_5.html',{"C_L":C_L,"Co_L":Co_L,"List":List}) 
