describe('Testando botao enviar', () => {
  it('"Enviado com sucesso!" -> apos validar botao', () => {

    cy.visit('http://localhost:8080/pagina.html'); 

    cy.get('#botaoEnviar').should('be.visible');

    cy.get('#botaoEnviar').click();
    cy.get('#mensagem').should('have.text', 'Enviado com sucesso!');

  });
});
