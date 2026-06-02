from playwright.sync_api import sync_playwright, Page, Browser, Playwright
from sqlalchemy import Engine
from Procesos.consulta import actualiza_tlmk


def Acceso_tlmk(usuario:str,password:str) -> tuple[Playwright, Browser, Page]:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://10.225.236.126/Telemarketing/Login.aspx")
    page.wait_for_selector("#txtUsuario")
    page.locator("#txtUsuario").fill(usuario)
    page.locator("#txtPassword").fill(password)
    page.locator("#btnLogin").click()
    page.get_by_text("Usuarios").click()
    page.wait_for_timeout(1000)
    return playwright,browser,page

def crear_usuarios(page:Page,usuariotlmk:str,nombre:str,password:str,id_usuario:int,engine:Engine) -> None:
    page.locator("#ib_Administracion").click()
    page.wait_for_selector("#txtBuscar")
    page.locator("#txtBuscar").fill(usuariotlmk)
    page.locator("#btnBuscar").click()
    if page.locator("#btnNotificaOk").is_visible():
        page.locator("#btnNotificaOk").click()
        page.locator("#btnNuevo").click()
        page.locator("#txtNombre").fill(nombre)
        page.locator("#txtUsuario").fill(usuariotlmk)
        page.select_option("#ddlPerfil",value="3")
        page.locator("#txtPassword").fill(password)
        page.locator("#txtConfirma").fill(password)
        page.locator("#btnGuardar").click()
        page.locator("#btnNotificaOk").click()
        actualiza_tlmk(engine=engine,id=id_usuario)
    else:
        page.locator("#ib_Administracion").click()
        actualiza_tlmk(engine=engine,id=id_usuario)
    page.wait_for_timeout(1000)

def cierre_pagina(browser:Browser,playwright:Playwright) -> None:
    browser.close()
    playwright.stop()