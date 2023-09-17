<h1>Cadastro de Clientes de Loja</h1>

    <p>Este é um algoritmo Python que simula o cadastro de clientes e compras em uma loja. Ele permite o registro de informações detalhadas de clientes, incluindo nome, renda, endereço e documentos como CPF e RG. Além disso, ele possibilita o registro de compras para cada cliente, com informações como data da compra, valor total e quantidade de produtos adquiridos. O algoritmo é interativo, permitindo que o usuário cadastre quantas compras desejar para cada cliente.</p>

    <h2>Funcionalidades</h2>
    <ul>
        <li><strong>Cadastro de Clientes</strong>
            <ul>
                <li><strong>Nome:</strong> O algoritmo permite que o usuário insira o nome do cliente.</li>
                <li><strong>Renda:</strong> O usuário pode informar a renda do cliente, que é registrada como um valor em ponto flutuante (float).</li>
                <li><strong>Endereço:</strong> O endereço do cliente pode ser inserido.</li>
                <li><strong>Documentos:</strong> Os documentos são registrados como um objeto com os seguintes atributos:
                    <ul>
                        <li>CPF (Cadastro de Pessoa Física)</li>
                        <li>RG (Registro Geral)</li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>Registro de Compras</strong>
            <ul>
                <li>O usuário pode registrar compras para cada cliente, incluindo informações como a data da compra, valor total da compra e quantidade de produtos adquiridos.</li>
                <li>O algoritmo permite que o usuário cadastre múltiplas compras para o mesmo cliente, tornando-o flexível para lidar com diferentes cenários de compra.</li>
            </ul>
        </li>
    </ul>

    <h2>Como Usar</h2>
    <ol>
        <li>Execute o programa Python em um ambiente adequado.</li>
        <li>Escolha uma das opções do menu principal:
            <ul>
                <li><strong>1 - Cadastrar cliente:</strong> Para cadastrar um novo cliente com informações detalhadas.</li>
                <li><strong>2 - Remover:</strong> Para remover um cliente com base no CPF.</li>
                <li><strong>3 - Visualizar cadastro:</strong> Para visualizar o cadastro de clientes e suas compras.</li>
                <li><strong>0 - Finalizar Programa:</strong> Para encerrar o programa e salvar os dados no arquivo "cadastro.json".</li>
            </ul>
        </li>
        <li>Siga as instruções para cada opção do menu e insira as informações necessárias.</li>
        <li>O programa permite que você adicione quantas compras desejar para cada cliente, dando flexibilidade para registrar as informações de acordo com o seu cenário.</li>
        <li>Certifique-se de selecionar a opção "0" no menu principal para salvar todos os dados antes de encerrar o programa.</li>
    </ol>

    <h2>Arquivo de Dados</h2>
    <p>Os dados dos clientes e suas compras são armazenados em um arquivo chamado "cadastro.json". Este arquivo é utilizado para manter os dados entre as execuções do programa, garantindo que as informações sejam preservadas.</p>
