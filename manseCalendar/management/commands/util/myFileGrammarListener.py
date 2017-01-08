# Generated from myFileGrammar.g4 by ANTLR 4.6
import datetime
from antlr4 import *

# This class defines a complete listener for a parse tree produced by myFileGrammarParser.
class myFileGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by myFileGrammarParser#line.
    def enterLine(self, ctx):
        pass

    # Exit a parse tree produced by myFileGrammarParser#line.
    def exitLine(self, ctx):
        pass


    # Enter a parse tree produced by myFileGrammarParser#solarDate.
    def enterSolarDate(self, ctx):
        pass
    # Exit a parse tree produced by myFileGrammarParser#solarDate.
    def exitSolarDate(self, ctx):
        year = ctx.year().getText()
        month = ctx.month().getText()
        day = ctx.day().getText()

        self.lunar_date = {
            'year': year,
            'month': month,
            'day': day,
        }

    # Enter a parse tree produced by myFileGrammarParser#lunarDate.
    def enterLunarDate(self, ctx):
        pass

    # Exit a parse tree produced by myFileGrammarParser#lunarDate.
    def exitLunarDate(self, ctx):
        year = ctx.year().getText()
        month = ctx.month().getText()
        day = ctx.day().getText()
        month_kind = ctx.monthKind().getText()

        self.lunar_date = {
            'year': year,
            'month': month,
            'day': day,
            'month_kind': month_kind
        }


    # Enter a parse tree produced by myFileGrammarParser#date.
    def enterDate(self, ctx):
        pass

    # Exit a parse tree produced by myFileGrammarParser#date.
    def exitDate(self, ctx):
        pass


    # Enter a parse tree produced by myFileGrammarParser#monthKind.
    def enterMonthKind(self, ctx):
        pass

    # Exit a parse tree produced by myFileGrammarParser#monthKind.
    def exitMonthKind(self, ctx):
        pass


    # Enter a parse tree produced by myFileGrammarParser#year.
    def enterYear(self, ctx):
        pass

    # Exit a parse tree produced by myFileGrammarParser#year.
    def exitYear(self, ctx):
        pass


    # Enter a parse tree produced by myFileGrammarParser#month.
    def enterMonth(self, ctx):
        pass

    # Exit a parse tree produced by myFileGrammarParser#month.
    def exitMonth(self, ctx):
        pass


    # Enter a parse tree produced by myFileGrammarParser#day.
    def enterDay(self, ctx):
        pass

    # Exit a parse tree produced by myFileGrammarParser#day.
    def exitDay(self, ctx):
        pass


