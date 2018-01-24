import Gateador
   
class RamStats:
    def main(self):        
        first_summoner = raw_input("Enter a summoner name to begin search: ")
        gateador = Gateador.Gateador()
        gateador.seed(first_summoner)

if __name__ == "__main__":
    amigo = RamStats()
    amigo.main()
