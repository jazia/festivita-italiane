# Festività italiane

Calendario iCalendar in italiano delle festività nazionali italiane, dal **2026 al 2030**. A cura di jazia, a partire dal calendario 2026 preparato per Stupid Calendar.

## Link per l’abbonamento

Usare questo indirizzo nella funzione “Aggiungi calendario da URL” della propria app:

https://raw.githubusercontent.com/jazia/festivita-italiane/main/festivita_italia.ics

L’abbonamento conserva il collegamento al file: gli aggiornamenti pubblicati qui verranno riletti secondo la frequenza dell’app utilizzata. Scaricare e importare il file crea invece una copia che non si aggiorna da sola.

## Contenuto

13 eventi per anno: Capodanno, Epifania, Pasqua, Lunedì dell’Angelo, Festa della Liberazione, Festa dei Lavoratori, Festa della Repubblica, Ferragosto, San Francesco d’Assisi, Ognissanti, Immacolata Concezione, Natale e Santo Stefano.

- San Francesco d’Assisi è incluso il **4 ottobre**, festa nazionale dal **2026**.
- Pasqua e Pasquetta sono calcolate per ogni anno secondo il calendario gregoriano.
- Non sono inclusi i patroni locali, le vacanze scolastiche o ricorrenze non festive, come il 17 marzo e il 4 novembre.
- Le domeniche ordinarie non sono elencate come eventi; Pasqua è indicata esplicitamente.
- Nessun trasferimento automatico al lunedì quando una festività cade nel fine settimana.
- Eventi di giornata intera, senza allarmi, con disponibilità trasparente: non bloccano l’agenda.
- Nomi e descrizioni restano in italiano anche usando un’app configurata in un’altra lingua.

## Formato e manutenzione

Il file è UTF-8, con terminatori CRLF e righe ripiegate a un massimo di 75 ottetti. Le date finali sono esclusive, come richiesto da iCalendar. Gli UID dell’edizione originale 2026 sono mantenuti per evitare duplicati negli aggiornamenti; gli anni aggiuntivi hanno UID distinti.

`festivita_italia_2026_originale.ics` conserva il file di partenza. `genera_calendario.py` genera il feed 2026–2030 con Python 3, senza dipendenze esterne. Per rigenerarlo:

```sh
python genera_calendario.py
```

Per aggiornamenti futuri, mantenere gli UID degli eventi già pubblicati, aggiornare DTSTAMP quando si modifica un evento e controllare eventuali variazioni legislative. La copertura termina al 31 dicembre 2030: non è un calendario perpetuo. Le festività future riflettono le norme verificate il 4 ottobre 2026.

## Fonti di verifica

- [Governo italiano: festività e giornate nazionali](https://presidenza.governo.it/ufficio_cerimoniale/cerimoniale/giornate.html).
- [Legge 8 ottobre 2025, n. 151: festa nazionale di San Francesco d’Assisi, in vigore dal 1° gennaio 2026](https://www.gazzettaufficiale.it/eli/id/2025/10/10/25G00153/SG).
- [DPR 28 dicembre 1985, n. 792: festività religiose](https://www.normattiva.it/atto/caricaDettaglioAtto?atto.codiceRedazionale=085U0792&atto.dataPubblicazioneGazzetta=1985-12-31).
- [Ambasciata d’Italia a Nairobi: date delle festività 2026](https://ambnairobi.esteri.it/it/chi-siamo/gli-uffici/calendario-delle-festivita-per-lanno-2026/).

## Stupid Calendar

La stessa edizione è inclusa nell’app come calendario integrato, attivo per impostazione predefinita e disattivabile in Impostazioni → Calendari → Calendari integrati. La copia inclusa funziona offline e viene aggiornata con l’app; non è un abbonamento remoto. Non va aggiunto nuovamente il feed, per evitare doppioni.
