#!/usr/bin/env python
# encoding: utf-8
# @author: frankdevhub
# @contact: frankdevhub@gmail.com
# @blog: http://blog.frankdevhub.site
# @file: character.py
# @time: 2021/2/15 20:50

import logging as log
import re

from .encode import CharacterEncode

log.basicConfig(level=log.INFO)

class CharacterHelper:
    # 通用国际字符编码
    CN_CHARACTERS = "[\\u4E00-\\u9FA5]"  # 中文字符 CN_CHARACTERS
    EN_CHARACTERS = "[a-zA-Z]"  # 英文字符 EN_CHARACTERS
    EN_CAPITAL_CHARACTERS = "[A-Z]"  # 大写英文字符 EN_CAPITAL_CHARACTERS
    NUMERIC_CHARACTERS = "[0-9]"  # 数值类字符 NUMERIC_CHARACTERS
    SYMBOL_CHARACTERS = "[a-zA-Z0-9\\u4E00-\\u9FA5]"  # 符号类字符 SYMBOL_CHARACTERS

    @staticmethod
    def character_pattern_match(target: chr, expression: chr) -> bool:
        # 匹配字符对象
        pattern = re.compile(expression, re.M | re.I)
        matched = pattern.search(target)
        if matched:
            return True
        else:
            return False

    @staticmethod
    def is_chinese_character(target: chr) -> bool:
        # 判断是否是中文字符
        log.info('invoke method -> is_chinese_character()')
        matched = CharacterHelper.character_pattern_match(target, CharacterHelper.CN_CHARACTERS)
        return matched

    @staticmethod
    def is_simple_chinese_character(target: chr) -> bool:
        """
        判断是否是简体中文字符
        @param target:
        @return:
        """
        log.info('invoke method -> is_simple_chinese_character()')
        is_chinese = CharacterHelper.is_chinese_character(target)
        if is_chinese:
            is_tw = False  # 是否是繁体中文字符
            try:
                encode = CharacterEncode.GB2312.code_name
                decode_target = target.encode(encode).decode(encode)
                print(f'source character : {target}，decode(GB2312): {decode_target}')
                if target == decode_target:
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
                    print(f'character: {target} is not a simple chinese character '
                          f'(possible should be taiwanese character).')
        else:
            print(f'character: {target} is not a chinese character.')
            return False

    @staticmethod
    def is_taiwanese_character(target: chr) -> bool:
        """
        判断是否是繁体中文字符
        @param target:
        @return:
        """
        log.info('invoke method -> is_taiwanese_character()')
        is_chinese = CharacterHelper.is_chinese_character(target)
        if is_chinese:
            is_simple_cn = False  # 是否是中文简体字符
            try:
                encode = CharacterEncode.Big5.code_name
                decode_target = target.encode(encode).decode(encode)
                print(f'source character : {target}，decode(Big5): {decode_target}')
                if target == decode_target:
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
                    print(f'character: {target} is not taiwanese character '
                          f'(possible should be simple chinese character).')
        else:
            print(f'character: {target} is not a chinese character.')
            return False

    @staticmethod
    def is_english_character(target: chr) -> bool:
        """
        判断是否是英文字符
        @param target:
        @return:
        """
        log.info('invoke method -> is_english_character()')
        matched = CharacterHelper.character_pattern_match(target, CharacterHelper.EN_CHARACTERS)
        return matched

    @staticmethod
    def is_english_capital_character(target: chr) -> bool:
        """
        判断是否是英文大写字符
        @param target:
        @return:
        """
        log.info('invoke method -> is_english_capital_character()')
        matched = CharacterHelper.character_pattern_match(target, CharacterHelper.EN_CAPITAL_CHARACTERS)
        return matched

    @staticmethod
    def is_numeric_character(target: chr) -> bool:
        """
        判断是否是数值类字符
        @param target:
        @return:
        """
        log.info('invoke method -> is_numeric_character()')
        matched = CharacterHelper.character_pattern_match(target, CharacterHelper.NUMERIC_CHARACTERS)
        return matched

    @staticmethod
    def is_symbol_character(target: chr) -> bool:
        """
        判断是否是符号类字符
        @param target:
        @return:
        """
        log.info('invoke method -> is_symbol_character()')
        matched = CharacterHelper.character_pattern_match(target, CharacterHelper.SYMBOL_CHARACTERS)
        return matched
