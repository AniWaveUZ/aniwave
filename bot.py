import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from threading import Thread
from flask import Flask

TOKEN = "8424454632:AAFUdy9bmZetNjq5DfS-wxiirZZhrXCrs4s"

# 🚀 RENDERda proxy kerak emas, u juda tez va to'g'ridan-to'g'ri ishlaydi!
bot = telebot.TeleBot(TOKEN)

# MULTI-ANIME TOZA VIDEO BAZASI
ANIME_BAZASI = {
    # TAKOPINING ILK GUNOHI BAZASI
    "takabo_1": "BAACAgIAAxkBAAMeaikifnhqiZtIJGurn1xJ0yZSpTAAAoyfAAJqVElJ2cHW70c2XOU7BA",
    "takabo_2": "BAACAgIAAxkBAAP0aik-_eKfMmvpv4jXrPa56BEquusAArR9AAInDgFLM5k5ElzBa_E7BA",
    "takabo_3": "BAACAgIAAxkBAAP1aik-_VP1_ktgF2Hf3cNowCA3aWsAAu59AAIEW0BLmKyNhIw8phk7BA",
    "takabo_4": "BAACAgIAAxkBAAP2aik-_WA3gXodLwwg87vEYGEmSJEAAuKCAAIgTolLGua-PJeFPPc7BA",
    "takabo_5": "BAACAgQAAxkBAAP3aik-_bBMuCOdZjiOyLyVIjMpad0AAjoZAALWXTlSBH3iFDBugJM7BA",
    "takabo_6": "BAACAgQAAxkBAAP4aik-_f9nuCJkj9v6A99HPiM4ppcAAjsZAALWXTlS59ygar14IsY7BA",
    "takabo_7": "BAACAgQAAxkBAAP5aik-_W1U2IDny01xuDDwKLL5ryUAAksZAALWXTlSJP_9dKUoWh47BA",

    # G'URUR BILAN GULLAYDIGAN QIZ BAZASI
    "gurur_1": "BAACAgIAAxkBAAMxaikuXNcaSAU7UQfRDd2B0h6vfbIAAhygAAJqVElJaxTN41TCrXs7BA",
    "gurur_2": "BAACAgQAAxkBAAM6aikxKNRYLyEIMirfMEUCzAABxkqTAALjHAACZRK5U_X2GVvNQSiqOwQ",
    "gurur_3": "BAACAgQAAxkBAAM8aikxT4gX3-WTeTh2Z9UztU3rZuUAAukaAALJ0FBQYM-jTwmXe-87BA",
    "gurur_4": "BAACAgQAAxkBAAM9aikxTwY2fRNx_KNO9dTuDTS4LJoAAhwcAAJmhYhQ5rzkhpYycvE7BA",
    "gurur_5": "BAACAgQAAxkBAAM9aikxTwY2fRNx_KNO9dTuDTS4LJoAAhwcAAJmhYhQ5rzkhpYycvE7BA",
    "gurur_6": "BAACAgQAAxkBAANBaikxiSmDu1HwzmbmCgSil95vjtwAAoQcAAI7BNlQQrLF5HHpfsk7BA",
    "gurur_7": "BAACAgQAAxkBAANCaikxiep00anUiI8-oVsFegpbx3MAAhccAAIGxjBR_jgtdnmcI747BA",
    "gurur_8": "BAACAgQAAxkBAANDaikxidWAxsbSy8Uz6tl2-XoEJU8AAmocAAIoEXBRPWPzJhNp5DE7BA",
    "gurur_9": "BAACAgQAAxkBAANEaikxibiTVkJvO6MS-mUpNvCJE0sAAr4cAAIUubhRyY0I1jbndXM7BA",
    "gurur_10": "BAACAgQAAxkBAANFaikxiZ40TRhTLDkuNNIQ0JyYIEYAAp4bAAJ2EAlSWb_I0QrOHwk7BA",
    "gurur_11": "BAACAgQAAxkBAANGaikxic7qg625x5HQLPdZW1Jq_vEAAgoYAAJmuV1SnDDg1vuDsUQ7BA",
    "gurur_12": "BAACAgQAAxkBAANHaikxieW9w0egjlve-GS5YUzsMgEAApwYAAKkt5BShnhgqh2TB_k7BA",
    "gurur_13": "BAACAgQAAxkBAANIaikxicXwI0IubYXgjLpmGuYLxBAAAtYYAAJCn9FSWFiZtQ19KQM7BA",

    # HYOUKA BAZASI
    "hyouka_1": "BAACAgIAAxkBAAIBkWoplAZdj9wKTyk-FpXIL_OLKv2QAAIgXQACeacJS5yf5zqjCOHUOwQ",
    "hyouka_2": "BAACAgUAAxkBAAIBkmoplAbyHF9TsfQ4Weq4OCXR2lVBAAL-DAACGfXJVcROTeM7pEOpOwQ",
    "hyouka_3": "BAACAgUAAxkBAAIBk2oplAYifsFES64J0caPQ4ARR1orAAL_DAACGfXJVZ64_rYHbneZOwQ",
    "hyouka_4": "BAACAgUAAxkBAAIBlGoplAZ7PGMHAoNNatezPf9zJ2YBAAMNAAIZ9clV-MIBEYZDWvQ7BA",
    "hyouka_5": "BAACAgUAAxkBAAIBlGoplAZ7PGMHAoNNatezPf9zJ2YBAAMNAAIZ9clV-MIBEYZDWvQ7BA",
    "hyouka_6": "BAACAgUAAxkBAAIBlWoplAa1HrFq0_vWNCm6mbZZr5wrAAIBDQACGfXJVdviVed_cHmZOwQ",
    "hyouka_7": "BAACAgUAAxkBAAIBlWoplAa1HrFq0_vWNCm6mbZZr5wrAAIBDQACGfXJVdviVed_cHmZOwQ",
    "hyouka_8": "BAACAgUAAxkBAAIBmGoplAa_hlBNZHCk6w_zgmVoZhA0AAIFDQACGfXJVeZsQU7JnUvGOwQ",
    "hyouka_9": "BAACAgUAAxkBAAIBmWoplAZ8WMyK9FNy41l-C8D4BX2dAAIHDQACGfXJVWuDcV_uyuXCOwQ",
    "hyouka_10": "BAACAgQAAxkBAAIBmmoplAZi1RDxsvq9L1SEwM1W2OfjAAJVEQAC0NHBUQFyoQSCp-37OwQ",
    "hyouka_11": "BAACAgQAAxkBAAIBm2oplAZE-qqAEJ472sbk-0WMmGTIAAJWEQAC0NHBUXdiVVBq1kFOOwQ",
    "hyouka_12": "BAACAgUAAxkBAAIBnGoplAZTQX3EwTPSpKGnLWEtdHuXAAIIDQACGfXJVTgoLoVTdHUQOwQ",
    "hyouka_13": "BAACAgUAAxkBAAIBnGoplAZTQX3EwTPSpKGnLWEtdHuXAAIIDQACGfXJVTgoLoVTdHUQOwQ",
    "hyouka_14": "BAACAgUAAxkBAAIBnmoplAZ6IT6qAS7hTbIyn5Fov8-XAAILDQACGfXJVRz3fu_WykdYOwQ",
    "hyouka_15": "BAACAgUAAxkBAAIBn2oplAZNXcgf4STIpyVhpydlXwfsAAIRDQACGfXJVeExCOXu5JSNOwQ",
    "hyouka_16": "BAACAgUAAxkBAAIBoGoplAaQQGNV1if2zK_1xTcX66teAAISDQACGfXJVfMvlrFQUuYyOwQ",
    "hyouka_17": "BAACAgUAAxkBAAIBoWoplAauSNcFHPtixdE6atReO7CgAAIWDQACGfXJVdWxHoqvkqZnOwQ",
    "hyouka_18": "BAACAgUAAxkBAAIBomoplAZGgAex1ZwJtBu46nUS87RBAAIXDQACGfXJVTaUx4JALrJ9OwQ",
    "hyouka_19": "BAACAgUAAxkBAAIBo2oplAaiU3NsGSRSLnX0ARZsvujpAAIcDQACGfXJVQwNqKnZvrZ8OwQ",
    "hyouka_20": "BAACAgUAAxkBAAIBpGoplAZbdnhp0oya31SkpJMKoNHdAAIfDQACGfXJVWpoI9Q8TK8jOwQ",
    "hyouka_21": "BAACAgUAAxkBAAIBpWoplAZp9qX-iE4UYPPthFjV4lXYAAIgDQACGfXJVRNOAAGJTDT69jsE",
    "hyouka_22": "BAACAgUAAxkBAAIBpmoplAanCb3ovckqV12v_ry0AYmhAAIhDQACGfXJVb5CLAuJrLPUOwQ",

    # YOLG'IZ ROKER BAZASI
    "roker_1": "BAACAgIAAxkBAAIB-moqU0mLwdPkHkD9ixreu2F0RA-bAAJLcAACh2_wS-Ikr2kY7F49OwQ",
    "roker_2": "BAACAgIAAxkBAAIB-2oqU0mz2TZTuV21Exktr20Og4bsAAKWYQAC2S8wSdgoo5S4eZwcOwQ",
    "roker_3": "BAACAgIAAxkBAAIB_GoqU0m-ULVi3xQtQxBOex-FCUNLAAL5aQACSEJoSZMXB3RCyDtQOwQ",
    "roker_4": "BAACAgIAAxkBAAIB_WoqU0nhTtPvW-Utlfzg8vQhkoKdAAKyawACSEJoSXhenDQ2Ls-HOwQ",
    "roker_5": "BAACAgIAAxkBAAIBmoqU0nE4nG56x7osfay2bwG7BIyAAIQZQACqTSZSVAX7dGgFAp_OwQ",
    "roker_6": "BAACAgIAAxkBAAIB_2oqU0l_bX5IHopPGnkF6Wfy5gxxAALFZwACL2ewSY3v-Qncf5KKOwQ",
    "roker_7": "BAACAgIAAxkBAAICAAFqKlNJLFln__7XdHqOklN0XiHOBgACPWYAAmDp-UnztAtpTzEkGjsE",
    "roker_8": "BAACAgIAAxkBAAICAmoqU0l3YzMaVEGT0_MI9klZxjUuAALHZwACq1MBS_V4Q9aRo5QjOwQ",
    "roker_9": "BAACAgIAAxkBAAICBWoqU0kmaHBQ-JClQrjuO5OX3XmpAAIzcAAC89hBS8iYBqKl_O39OwQ",
    "roker_10": "BAACAgIAAxkBAAICA2oqU0kMUmK24ozXErqJsDDtU8rMAAI1lgACBAyBS5ac6LOUbcFjOwQ",
    "roker_11": "BAACAgIAAxkBAAICBGoqU0nIcaIi4w8mzrXcQgbDwYyPAAJJcAACh2_wS8Hm3ymjT5YdOwQ",
    "roker_12": "BAACAgIAAxkBAAICBWoqU0kmaHBQ-JClQrjuO5OX3XmpAAIzcAAC89hBS8iYBqKl_O39OwQ"
}

ANIME_RASMLARI = {
    "gurur": "AgACAgIAAxkBAAIBL2opR5wJs2jc_3Yqbk_BKgNsdIQKAAKZGWsbuF5ISdRRG31BlP2iAQADAgADeAADOwQ", 
    "takabo": "AgACAgIAAxkBAAIBM2opSPI3i1tkqc4zwdtVeqfgyQfnAALrGWsbuF5QSRUdqqyLISuYAQADAgADeQADOwQ",
    "hyouka": "AgACAgIAAxkBAAICPmoqY9gRv9tzgExkck_KpiUxvYy7AAJnHGsbeHhQSdTn_tWXwSa6AQADAgADeQADOwQ", 
    "roker": "AgACAgIAAxkBAAICEmoqU1YFp0Ch1NxPCg8E4DtN6NvQAALcG2sbeHhQSaLXB6zHIFhpAQADAgADeQADOwQ"
}

@bot.message_handler(content_types=['video', 'photo', 'document'])
def get_file_ids(message):
    try:
        if message.video:
            f_id = message.video.file_id
            bot.reply_to(message, f"✅ *Video ID-si:* `{f_id}`", parse_mode="Markdown")
        elif message.photo:
            f_id = message.photo[-1].file_id
            bot.reply_to(message, f"✅ *Rasm ID-si:* `{f_id}`", parse_mode="Markdown")
        elif message.document:
            f_id = message.document.file_id
            bot.reply_to(message, f"✅ *Hujjat ID-si:* `{f_id}`", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('p_'))
def send_anime_part(call):
    anime_kodi = call.data.replace('p_', '')
    if anime_kodi in ANIME_BAZASI:
        bot.answer_callback_query(call.id, "Anime yuklanmoqda... ⏳")
        if "takabo" in anime_kodi:
            qism_raqami = anime_kodi.replace('takabo_', '')
        elif "gurur" in anime_kodi:
            qism_raqami = anime_kodi.replace('gurur_', '')
        elif "hyouka" in anime_kodi:
            qism_raqami = anime_kodi.replace('hyouka_', '')
        elif "roker" in anime_kodi:
            qism_raqami = anime_kodi.replace('roker_', '')
        else:
            qism_raqami = ""
        caption_text = f"🎬 {qism_raqami}-qism sizga maroqli tomosha!" if qism_raqami else "🎬 Maroqli tomosha!"
        try:
            bot.send_video(call.message.chat.id, ANIME_BAZASI[anime_kodi], caption=caption_text)
        except Exception as e:
            bot.send_message(call.message.chat.id, f"Xatolik: {e}")
    else:
        bot.answer_callback_query(call.id, "Kechirasiz, video topilmadi! ❌", show_alert=True)

@bot.message_handler(commands=['start'])
def handle_start(message):
    matn_qismlari = message.text.split()
    if len(matn_qismlari) == 1:
        channel_markup = InlineKeyboardMarkup()
        channel_btn = InlineKeyboardButton("📢 Kanalga o'tish", url="https://t.me/AniwaveUZ")
        channel_markup.add(channel_btn)
        bot.send_message(message.chat.id, "Salom! Animeni ko'rish uchun kanaldagi maxsus linklarni bosing. 🎬", reply_markup=channel_markup)
        return
    
    anime_kodi = matn_qismlari[1]
    
    if anime_kodi == "gurur":
        markup = InlineKeyboardMarkup(row_width=3)
        tugmalar = [InlineKeyboardButton(f"{i}-Qism", callback_data=f"p_gurur_{i}") for i in range(1, 14)]
        markup.add(*tugmalar)
        matn = "✨ *G'urur bilan gullaydigan qiz* animesi topildi!\n\ntugmalardan birini tanlang 👇"
        try:
            bot.send_photo(message.chat.id, ANIME_RASMLARI["gurur"], caption=matn, reply_markup=markup, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, matn, reply_markup=markup, parse_mode="Markdown")
    elif anime_kodi == "takabo":
        markup = InlineKeyboardMarkup(row_width=3)
        tugmalar = [InlineKeyboardButton(f"{i}-Qism", callback_data=f"p_takabo_{i}") for i in range(1, 8)]
        markup.add(*tugmalar)
        matn = "🌌 *Takopining ilk gunohi* animesi topildi!\n\ntugmalardan birini tanlang 👇"
        try:
            bot.send_photo(message.chat.id, ANIME_RASMLARI["takabo"], caption=matn, reply_markup=markup, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, matn, reply_markup=markup, parse_mode="Markdown")
    elif anime_kodi == "hyouka":
        markup = InlineKeyboardMarkup(row_width=3)
        tugmalar = [InlineKeyboardButton(f"{i}-Qism", callback_data=f"p_hyouka_{i}") for i in range(1, 23)]
        markup.add(*tugmalar)
        matn = "🔍 *Hyouka* animesi topildi!\n\ntugmalardan birini tanlang 👇"
        try:
            bot.send_photo(message.chat.id, ANIME_RASMLARI["hyouka"], caption=matn, reply_markup=markup, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, matn, reply_markup=markup, parse_mode="Markdown")
    elif anime_kodi == "roker":
        markup = InlineKeyboardMarkup(row_width=3)
        tugmalar = [InlineKeyboardButton(f"{i}-Qism", callback_data=f"p_roker_{i}") for i in range(1, 13)]
        markup.add(*tugmalar)
        matn = "🎸 *Yolg'iz Roker* animesi topildi!\n\ntugmalardan birini tanlang 👇"
        try:
            bot.send_photo(message.chat.id, ANIME_RASMLARI["roker"], caption=matn, reply_markup=markup, parse_mode="Markdown")
        except Exception as e:
            bot.send_message(message.chat.id, matn, reply_markup=markup, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "Afsuski, bu anime bazamizda topilmadi. ❌")

# Render portni tekshirishi uchun kichik Flask veb-server yaratamiz
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Veb-serverni alohida oqimda (thread) ishga tushiramiz
def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()  # Kichik veb-server ishga tushadi
    print("Bot muvaffaqiyatli yoqildi!")
    bot.infinity_polling(none_stop=True, timeout=60, long_polling_timeout=30)
