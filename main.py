from functions import *
from params import *

if __name__ == '__main__':
    # pobranie z api aktualnej listy przystankow
    stops = get_actual_stops_info(stops_list_url)

    # pobranie z api odjazdów
    response = get_data_from_api(departures_url)
    departures = transform_departures(response)

    # obrabianie danych
    final_df = (departures[departures.status == 'REALTIME']
        .sort_values('stopId')
        .drop(['scheduledTripStartTime',
                'status',
                'theoreticalTime',
                'vehicleService',
                ], axis=1)
        .merge(stops, on='stopId')
        .assign(headsign=lambda x: x.headsign.apply(removeAccents),
                estimatedTime=lambda x: pd.to_datetime(
                    x.estimatedTime, format='%Y-%m-%d %H:%M:%S').dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                timestamp=lambda x: pd.to_datetime(
                    x.timestamp, format='%Y-%m-%d %H:%M:%S').dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
                lastUpdate=lambda x: pd.to_datetime(x.lastUpdate, format='%Y-%m-%d %H:%M:%S').dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
        .drop(['stopId'], axis=1)
        .reset_index(drop=True)
    )

    # laczenie tabel z przystankami z tabela z aktualnymi opoznieniami
    post_data_to_pbi(final_df, pbi_api, headers)

