#!/usr/bin/env python
# encoding: utf-8
# @author: frankdevhub
# @contact: frankdevhub@gmail.com
# @blog: http://blog.frankdevhub.site
# @file: character.py
# @time: 2021/2/15 20:50

import logging as log
import re

from encode import CharacterEncode
log.basicConfig(level=log.INFO)

class CharacterHelper:
    # 通用国际字符编码
    CN_CHARACTERS = "[\\u4E00-\\u9FA5]"  # 中文字符 CN_CHARACTERS
    EN_CHARACTERS = "[a-zA-Z]"  # 英文字符 EN_CHARACTERS
    EN_CAPITAL_CHARACTERS = "[A-Z]"  # 大写英文字符 EN_CAPITAL_CHARACTERS
    NUMERIC_CHARACTERS = "[0-9]"  # 数值类字符 NUMERIC_CHARACTERS
    SYMBOL_CHARACTERS = "[a-zA-Z0-9\\u4E00-\\u9FA5]"  # 符号类字符 SYMBOL_CHARACTERS

    @staticmethod
    def character_pattern_match(char: chr, expression: chr) -> bool:
        # 匹配字符对象
        pattern = re.compile(expression, re.M | re.I)
        matched = pattern.search(char)
        if matched:
            return True
        else:
            return False

    @staticmethod
    def is_chinese_character(char):
        # 判断是否是中文字符
        matched = CharacterHelper.character_pattern_match(
            char, CharacterHelper.CN_CHARACTERS)
        return matched

    @staticmethod
    def is_simple_chinese_character(char):
        is_chinese = CharacterHelper.is_chinese_character(char)
        if is_chinese:
            is_tw = False  # 是否是繁体中文字符
            try:
                encode = CharacterEncode.GB2312.code_name
                decode_char = char.encode(encode).decode(encode)
                print(
                    f'source character : {char}，decode(GB2312): {decode_char}')
                if char == decode_char:
                    return True
                else:
                    is_tw = True
                    return False
            except Exception as e:
                is_tw = True
                log.error(str(e))
                return False
            finally:
                if is_tw:
                    print(f'character: {char} is not a simple chinese character '
                          f'(possible should be taiwanese character).')
        else:
            print(f'character: {char} is not a chinese character.')
            return False

    @staticmethod
    def is_taiwanese_character(char):
        log.info('invoke method -> is_taiwanese_character()')
        is_chinese = CharacterHelper.is_chinese_character(char)
        if is_chinese:
            is_simple_cn = False  # 是否是中文简体字符
            try:
                encode = CharacterEncode.Big5.code_name
                decode_char = char.encode(encode).decode(encode)
                print(
                    f'source character : {char}，decode(Big5): {decode_char}')
                if char == decode_char:
                    return True
                else:
                    is_simple_cn = False
                    return False
            except Exception as e:
                is_simple_cn = True
                log.error(str(e))
                return False
            finally:
                if is_simple_cn:
                    print(f'character: {char} is not taiwanese character '
                          f'(possible should be simple chinese character).')
        else:
            print(f'character: {char} is not a chinese character.')
            return False

    @staticmethod
    def is_english_character(char):
        matched = CharacterHelper.character_pattern_match(
            char, CharacterHelper.EN_CHARACTERS)
        return matched

    @staticmethod
    def is_english_capital_character(char):
        matched = CharacterHelper.character_pattern_match(
            char, CharacterHelper.EN_CAPITAL_CHARACTERS)
        return matched

    @staticmethod
    def is_numeric_character(char):
        matched = CharacterHelper.character_pattern_match(
            char, CharacterHelper.NUMERIC_CHARACTERS)
        return matched

    @staticmethod
    def is_symbol_character(char):
        # 判断是否是符号类字符
        matched = CharacterHelper.character_pattern_match(
            char, CharacterHelper.SYMBOL_CHARACTERS)
        return matched
