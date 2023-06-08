class Operation:

    def __init__(self, num, state, date, description, out, to, amount):
        self.num = num
        self.state = state
        self.date = date
        self.description = description
        self.out = out
        self.to = to
        if amount != "-":
            self.amount = amount["amount"]
            self.currency_name = amount["currency"]["name"]
            self.currency_code = amount["currency"]["code"]
        else:
            self.amount = "-"
            self.currency_name = "-"
            self.currency_code = "-"

    def get_date(self):
        """
        Поеборазует дату в установленный формат: ДД.ММ.ГГГГ
        :return: str
        """
        datatime_list = self.date.split("T")
        date_without_time = datatime_list[0]
        data_list = date_without_time.split("-")
        inverted_date = data_list[::-1]
        data = ".".join(inverted_date)
        return data

    def mask_from(self):
        """
        Маскирует номер счета или карты, откуда производится списание
        :return: str
        """
        if self.out != "-":
            out_split = self.out.split(" ")
            if "Счет" in out_split:
                account = out_split[-1]
                mask_account = f"****{account[-4:]}"
                return f"{out_split[0]} {mask_account}"
            else:
                card = out_split[-1]
                if len(out_split) > 2:
                    card_name = " ".join(out_split[:2])
                else:
                    card_name = out_split[0]
                return f"{card_name} {card[:4]} {card[4:6]}** **** {card[-4:]}"
        else:
            return "cash"

    def mask_to(self):
        """
        Маскирует номер счета или карты, куда производится зачисление
        :return: str
        """
        if self.to != "-":
            to_split = self.to.split(" ")
            if "Счет" in to_split:
                account = to_split[-1]
                mask_account = f"****{account[-4:]}"
                return f"{to_split[0]} {mask_account}"
            else:
                card = to_split[-1]
                if len(to_split) > 2:
                    card_name = " ".join(to_split[:2])
                else:
                    card_name = to_split[0]
                return f"{card_name} {card[:4]} {card[4:6]}** **** {card[-4:]}"
        else:
            return "cash"

    def __repr__(self):
        return f"{self.get_date()} {self.description}\n" \
               f"{self.mask_from()} -> {self.mask_to()}\n" \
               f"{self.amount} {self.currency_name}\n"
