from .request import Requester

class Responser(Requester):
    def history_to_message(self) -> str:
        return self.get_history()

    def status_to_message(self):
        (status, ok) = self.get_status()
        if ok:
            return (status, ok)
        else:
            return (f"{status}\n{self.get_payment_link()}", ok)
    
    def confirm_to_message(self):
        is_confirmed = self.confirm()
        if is_confirmed:
            return self.get_status()

    def instruction_to_message(self) -> str:
        return "тут пока ничего нет"

    def info_to_message(self) -> str:
        return "тут пока ничего нет"

    def start_to_message(self) -> str:
        return "привет"

    def help_to_message(self) -> str:
        return "Тут пока ничего нет"

    def cansel_to_message(self) -> str:
        return "👌"

    def other_to_message(self) -> str:
        return "-_-"
    
    def paid_to_message(self):
        ok = self.confirm()
        if ok:
            return "Подтверждено"
        else:
            return "Не подтверждено"
