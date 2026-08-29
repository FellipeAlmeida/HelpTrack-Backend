class UserNotFound(Exception):
    def __init__(self, message='Usuário não encontrado.'):
        super().__init__(message)
        self.message = message

class CompanyNotFound(Exception):
    def __init__(self, message='Empresa não encontrada.'):
        super().__init__(message)
        self.message = message

class ExistingCompany(Exception):
    def __init__(self, message='Empresa já cadastrada.'):
        super().__init__(message)
        self.message = message

class CredentialsError(Exception):
    def __init__(self, message='Credenciais Inválidas.'):
        super().__init__(message)
        self.message = message

class UserNotActive(Exception):
    def __init__(self, message='Usuário não ativo, solicite a um admin para ativar sua conta novamente.'):
        super().__init__(message)
        self.message = message

class UserBlocked(Exception):
    def __init__(self, tempo_bloqueado):
        self.message = f'Usuário bloqueado até {tempo_bloqueado}.'
        super().__init__(self.message)

class TokenError(Exception):
    def __init__(self, message='Token inválido ou expirado'):
        super().__init__(message)
        self.message = message

class UserNotAuthorized(Exception):
    def __init__(self, message='Não autorizado.'):
        super().__init__(message)
        self.message = message

class InvalidData(Exception):
    def __init__(self, message='Dados inválidos.'):
        super().__init__(message)
        self.message = message

class ExistingAccount(Exception):
    def __init__(self, message='Conta já cadastrada.'):
        super().__init__(message)
        self.message = message