d_message = input("rentrez votre texte:")
clef = int(input("rentrez votre cle :"))
message = []
message_décodé = []
for i in d_message:
    message.append(ord(i)+clef)
for i in message:
    message_décodé.append(chr(i))
final ="".join(message_décodé)
print(final)