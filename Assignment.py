{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "gen_words\n",
      "Welcome To Word Fix.Unscramble the letters to make a word.\n",
      "ur_beEolsgr[dnsihwm]n"
     ]
    }
   ],
   "source": [
    "# The computer picks a random and then jumble it\n",
    "# The player has to guess the original world\n",
    "english_words=(\"C:\\\\Users\\\\IKUBE\\\\Anaconda3\\\\Words.txt\")\n",
    "def rand_word():\n",
    "    with open(\"C:\\\\Users\\\\IKUBE\\\\Anaconda3\\\\Words.txt\") as word_file:\n",
    "        english_words = list(word.strip().lower() for word in word_file)\n",
    "    \n",
    "import random\n",
    "gen_words = english_words\n",
    "number = random.randint(0, 370099)\n",
    "gen_words = \"English_words[number]\"\n",
    "print(\"gen_words\")\n",
    "shuf_word = list(n for n in gen_words)\n",
    "random.shuffle(shuf_word)\n",
    "print('Welcome To Word Fix.Unscramble the letters to make a word.')\n",
    "for n in shuf_word:\n",
    "    print(n, sep=\"\", end=\"\")\n",
    "while True:\n",
    "    answer = input(\"Start Game\\n Input the correct word here: \")\n",
    "    if answer == gen_words:\n",
    "        print(\"Thats Sway Fam\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"wrong! try again\")\n",
    "        print(\"The word is: ()\".format(gen_words))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
