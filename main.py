import datetime;

print("Lol", 555, "999");
print(print);
# name = input("Enter someThing: ");
# print(name )
lol = "Lol";
print(dir(lol))
x = 777;
print(dir(x));
print(lol.upper());

print(dir())
print(dir(__builtins__))
# input("Enter name, please: ");
# zzz = input("Enter name, please: ");
# ddd = input("age: ")
# aaa = input("Your cource: ")
# print(zzz + " " + ddd + " " + " " + aaa);
# print(zzz.capitalize());


def myFn():
    print("Hello");

print("Lol");

myFn();

print(datetime.MAXYEAR);
print(datetime.MINYEAR);

a = 10;
b = 3;


def myInstr(a, b):
    return a * b + 100;


f = myInstr(a, b);

print(f);

name_lol = "Lol!!!";
print(name_lol);
name_lol = "1234567890";
name_lol2 = "abcdefgh";
print(name_lol);

id(lol);

dal = lol;
print(id(lol));
print(id(dal));

pop = "Lol";
print(id(pop));
top = True;

print(type(pop));
print(type(b));
print(type(top));

ppp = "lol" \
      "lol      " \
      "555";
zzz = """ I
        soo
all
   good
"""
print(ppp);
print(zzz);
print(type(zzz));
print(type(int));
print(id(zzz))
# print(type(function));

print(len(name_lol));

print(name_lol[0]);
print(name_lol[1]);
print(name_lol[2]);
print(name_lol[3]);
print(name_lol[5 : 8]);
print(name_lol[:6]);
print(name_lol[4:]);
print(name_lol.count(name_lol));
print(name_lol2.upper());
print(name_lol2.count("bcdef"));  #содержит ли, аналог контэйн
name_new = name_lol2.replace("abc", "123");
print(name_new);
print(ppp.count("  "));  #количество данного выражения в нашей переменной 3*2  "  "
print(ppp[-2]);
print(ppp[3: -2]);
print(ppp[-2: ]);

x = "555";
x = int(x);
print(type(x));
x += 7.88888;
print(x);
print(type(x));

print(pow(2, 10));  #2 в 10 степени 1024
zz = 1_000_000;
print(zz + x);

# qqq = input("Enter num: ")
qqq = 100;
print(type(qqq));
qqq = int(qqq);
print(type(qqq));

cc = 0.2+0.3+0.4+0.5+0.6+0.1+0.7
print(cc);
print(type(cc));

bb = "444.444";
cc = float(bb);
rr =  str(bb) + " hello " + str(type(bb));
print(rr);

x = 66.66;
print(x.__round__());
print(round(x));

k = 2;
complex_x = 10 + 9j;
complex_y = 20 + 10j;

print(str( complex_y + complex_x) + " and "+ str(type(complex_y)));

print ("lll" < "z")

print([1,2,3,9] > [1,9]);
print({a: 6} == {a: 6});

ss = 2;
ee = 2.5;
print(ss+ee);
print(ee+ss);

nnn = True;
bbb = 7;
print(nnn + bbb);
print(bbb+nnn);

gg = "Lob ";
g = 10;
# print(g * gg);
# print(gg * g);

print(g.__mul__(gg));   #NotImplemented
print(gg.__mul__(g));   #Lob Lob Lob Lob Lob Lob Lob Lob Lob Lob
print(gg.__rmul__(g));  #Lob Lob Lob Lob Lob Lob Lob Lob Lob Lob
print(bool.__doc__);

my_list = [];
print("!!!")
print(my_list.__doc__);
print(help(my_list.__eq__));
print(my_list.__eq__);

list_fruits = ["apple", "banana", "lime"];
number_list_1 = [100, 300, 1000];
number_list_2 = [1000, 300, 100];
user_input_list = ["Hello", 100, True, 99.99];

print(number_list_1 == number_list_2);  #False
print(number_list_1.__len__());
print(len(number_list_2));
print(len(number_list_2) == len(number_list_1));
print(user_input_list[-2]);
print(user_input_list[3]);
print(user_input_list[2] == user_input_list[-2]);
user_input_list[-2] = False
print(user_input_list[-2]);
del user_input_list[-2];
print(user_input_list);

users = [
    {
        "id_user": 888,
        "name_user": "Ann"
    },
    {
        "id_user": 891,
        "name_user": "Tom"
    }
];



print(len(users));
print(users);
print(users[0]);
print(users[1]);

user_inputs = [True, "Lol", 33.33, 100];
ff = user_inputs.pop();
print(str(user_inputs) + " ! " + str(ff));
user_inputs.pop(-2);
print(user_inputs);
user_inputs.append("SuperLol");
print(user_inputs);
# user_inputs.sort();
# print(user_inputs);
# user_inputs.sort(reverse=True);
# print(user_inputs);
print("!!!@@@@@@@@")
num_different = [55, -99, -999, 567];
num_different.sort();
print(num_different);
print(min(num_different));
print(max(num_different));
print(sum(num_different));
print(sum(num_different)/len(num_different));
num_different2 = [10, 10];
num_different3 = num_different2 + num_different;
print(num_different3);
num_different4 = num_different2.__add__(num_different).__add__(num_different3);
print(num_different4);


# num_different.sort();
print(num_different);
num_different.sort(reverse=True);
print(num_different);
str_some = ["qwe", "abc", "aaa", "zzz", "azzz"];
str_some.sort();
print(str_some);
some_text = "Hello world for ever";
some_text_lettes = list(some_text);
print(some_text_lettes);

users2 ={ "id_user": 888,
          "name_user": "Ann" };
print(users2);
users_letters = list(users2);
print(users_letters);

num_different5 = num_different4[:3];
print(num_different5)
num_different6 = num_different4[2: -2];
print(num_different4);
print(num_different6);
num_different7 = num_different4[:];
print(num_different7);
num_different8 = num_different7;
print(id(num_different4));
print(id(num_different7));
print(id(num_different8));
num_different9 = num_different4.copy();
print(id(num_different9));
num_different10 = list(num_different4);
print(id(num_different10));
print(num_different10.count(10));
num_different10.append(888);
print(num_different10);
num_different10.insert(2, -666);
print(num_different10);
num_different10.extend("abc");
print(num_different10);