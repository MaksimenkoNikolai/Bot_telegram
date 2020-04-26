{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import telebot\n",
    "\n",
    "bot=telebot.TeleBot('1165724384:AAG_-gHoio1fUwRrP-A3Pf4kXxH33GcuCgs')\n",
    "\n",
    "@bot.message_handliner(content_types=['text'])\n",
    "def lalala(message):\n",
    "    bot.send_message(message.chat.id, message.text)\n",
    "\n",
    "#RUN\n",
    "bot.polling(none_stop=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
