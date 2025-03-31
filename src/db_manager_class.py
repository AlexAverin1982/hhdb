"""
Класс DBManager будет подключаться к БД PostgreSQL

Класс 
DBManager
 должен использовать библиотеку 
psycopg2
 для работы с БД.
"""
class DBManager:
    def __init__(self):
        pass
        
    def get_companies_and_vacancies_count(self) -> int:
        """
        — получает список всех компаний и количество вакансий у каждой компании.
        """
        result = 0
        return result
    
    def get_all_vacancies(self) -> list:
        """
        — получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        result = []
        return result
    
    def get_avg_salary(self) -> int:
        """
        — получает среднюю зарплату по вакансиям.
        """
        result = 0
        return result
    
    def get_vacancies_with_higher_salary(self) -> list:
        """
        — получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        result = []
        return result

    def get_vacancies_with_keyword(self) -> list:
        """
        — получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        """
        result = []
        return result
