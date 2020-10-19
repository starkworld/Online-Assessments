import json
import copy
from collections import defaultdict


# Implement the class below, keeping the constructor's signature unchanged; it should take no arguments.


# Implement the class below, keeping the constructor's signature unchanged; it should take no arguments.
class Company:
    def __init__(self, name):
        self.name = name
        self.own = 0
        self.sell = 0
        self.buy = 0

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class MarkingPositionMonitor:
    def __init__(self):
        self.company_dict = {}
        self.order_dict = {}

    def on_event(self, message):
        m_dict = json.loads(message)

        if m_dict["type"] == "NEW":
            company_name = m_dict["symbol"]
            order_id = m_dict["order_id"]
            self.order_dict[order_id] = m_dict
            # create company instance in dict if not exist.
            if company_name not in self.company_dict:
                self.company_dict[company_name] = Company(company_name)
            # immediately change the quantity.
            if m_dict["side"] == "SELL":
                self.company_dict[company_name].sell += int(m_dict["quantity"])
            # new order to buy does not affect marking postion.
            if m_dict["side"] == "BUY":
                self.company_dict[company_name].buy += int(m_dict["quantity"])
            return self.company_dict[company_name].own - self.company_dict[company_name].sell

        if m_dict["type"] == "ORDER_REJECT":
            # read the history order message detail from order_id
            order_id = m_dict["order_id"]
            order_detail = self.order_dict[order_id]
            company_name = order_detail["symbol"]
            if order_detail["type"] == "NEW":
                # immediately change sell quantity
                if order_detail["side"] == "SELL":
                    self.company_dict[company_name].sell -= int(order_detail["quantity"])
                if order_detail["side"] == "BUY":
                    self.company_dict[company_name].buy -= int(order_detail["quantity"])
            return self.company_dict[company_name].own - self.company_dict[company_name].sell

        if m_dict["type"] == "ORDER_ACK":
            order_id = m_dict["order_id"]
            order_detail = self.order_dict[order_id]
            company_name = order_detail["symbol"]
            # acknowledge order, no further action need to take though.
            if order_detail["side"] == "SELL":
                pass
            if order_detail["side"] == "BUY":
                pass
            return self.company_dict[company_name].own - self.company_dict[company_name].sell

        if m_dict["type"] == "CANCEL":
            # try to cancel stated; no immediate effect.
            order_id = m_dict["order_id"]
            order_detail = self.order_dict[order_id]
            company_name = order_detail["symbol"]
            if order_detail["type"] == "NEW":
                if order_detail["side"] == "SELL":
                    pass
                if order_detail["side"] == "BUY":
                    pass
                return self.company_dict[company_name].own - self.company_dict[company_name].sell

        if m_dict["type"] == "CANCEL_ACK":
            # cancellation acknowledged; the order is no longer in the market; immediate effect.
            order_id = m_dict["order_id"]
            order_detail = self.order_dict[order_id]
            company_name = order_detail["symbol"]
            if order_detail["type"] == "NEW":
                # immediately change the quantity; immediate effect.
                if order_detail["side"] == "SELL":
                    self.company_dict[company_name].sell -= int(order_detail["quantity"])
                if order_detail["side"] == "BUY":
                    self.company_dict[company_name].buy -= int(order_detail["quantity"])
                return self.company_dict[company_name].own - self.company_dict[company_name].sell

        if m_dict["type"] == "CANCEL_REJECT":
            # reject cancellation; no effect.
            order_id = m_dict["order_id"]
            order_detail = self.order_dict[order_id]
            company_name = order_detail["symbol"]
            if order_detail["type"] == "NEW":
                if order_detail["side"] == "SELL":
                    pass
                if order_detail["side"] == "BUY":
                    pass
                return self.company_dict[company_name].own - self.company_dict[company_name].sell

        if m_dict["type"] == "FILL":
            order_id = m_dict["order_id"]
            order_detail = self.order_dict[order_id]
            company_name = order_detail["symbol"]
            if order_detail["type"] == "NEW":
                if "filled_quantity" not in order_detail:
                    order_detail["filled_quantity"] = 0
                if order_detail["side"] == "SELL":
                    order_detail["filled_quantity"] = m_dict["filled_quantity"]
                if order_detail["side"] == "BUY":
                    self.company_dict[company_name].own -= order_detail[
                        "filled_quantity"]  # minus bought quantity from this order
                    order_detail["filled_quantity"] = m_dict["filled_quantity"]
                    self.company_dict[company_name].own += order_detail[
                        "filled_quantity"]  # add current bought quantity from this order

                return self.company_dict[company_name].own - self.company_dict[company_name].sell

        return 0  # return 0 for not handled operations


def assertEqual(a, b):
    if a != b:
        print("False! ", a, b)
    else:
        print(a)


if __name__ == '__main__':
    M = MarkingPositionMonitor()
