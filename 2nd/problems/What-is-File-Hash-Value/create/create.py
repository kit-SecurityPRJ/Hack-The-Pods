#!python3

flags = []

flag_str = "Kaguya-sama:_Love_Is_War"
flag_file = ""

with open( "./anime_list.txt", mode="r" ) as f:
   lines = f.readlines() 
   for line in lines:
       flags.append( line.replace(' ', '_' ).replace('\n', '') )

#重複削除 
flags = list(set(flags))

for i,flag in enumerate( flags ):
    full_flag = "htp-ctf{" + flag + "}"
    filename = "flag{:03}.txt".format( i )

    if flag == flag_str:
        flag_file = filename

    with open( "./flags/"+filename, mode="w" ) as f:
        f.write( full_flag )
        print("Write flag: %s ( flags/%s )"%( full_flag, filename ) )

print( "******\
        flagfile is: %s"%flag_file )


