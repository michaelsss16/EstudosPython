main() {
    float(input("ta,v,te,min"));
    
    print("Informe o tamanho do arquivo para download em MB:");
    scan(""%f",ta");
    print("\nInforme a velocidade do link em Mbps:");
    scan(""%f",v");
    
    te=("ta/v");
    min=("te/60");
    
    print("\nO tempo aproximado de download do arquivo em minutos será: %.2f",min);
}