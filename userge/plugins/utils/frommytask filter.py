#tasker filter for dbbots gro... keyword is frommytask
 
from userge import userge, Message 
from pyrogram import filters 
 
@userge.on_message(filters.incoming & filters.chat(-1001151927732) & filters.regex(pattern=r"frommytask")) 
async def xyz_abc(_, message: Message): 
    txt = "/mirror@lzzy12_dbbot " 
    txt += message.text 
    await userge.send_message(message.chat.id, text=txt)