from pagamento import *
from pagamentoContanti import *
from pagamentoCredito import *


def main()->None:
    pc:PagamentoContanti = PagamentoContanti(150.00)
    pc.dettagliPagamento()
    pc.inPezziDa()
    print()
    pc1:PagamentoContanti = PagamentoContanti(95.25)
    pc1.dettagliPagamento()
    pc1.inPezziDa()
    print()
    scadenza:date = date(2024, 12, 22)
    pcr:PagamentoCartaDiCredito = PagamentoCartaDiCredito(200.00, 'Mario Rossi', scadenza, 1234567890123456)
    pcr.dettagliPagamento()
    print()
    scadenza1:date = date(2025, 1,31)
    pcr1:PagamentoCartaDiCredito = PagamentoCartaDiCredito(500.00, 'Luigi Bianchi', scadenza1, 6543210987654321)
    pcr1.dettagliPagamento()

if __name__ == "__main__":
    main()