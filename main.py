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



