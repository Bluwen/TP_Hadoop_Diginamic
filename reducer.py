#!/usr/bin/env python3
import sys
import happybase

try:
    connection = happybase.Connection('hadoop-master')
    tables = connection.tables()

    if b'dance_energy_stats' not in tables:
        connection.create_table('dance_energy_stats', {'cf': dict()})
    table = connection.table('dance_energy_stats')
except Exception as e:
    print("HBase connection error: {0}".format(e), file=sys.stderr)
    sys.exit(1)

current_danceability = None
current_energy = None
total_streams = 0
total_count = 0

try:
    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) != 3:
            continue  # skip malformed lines

        danceability, energy, streams = parts
        try:
            streams = int(streams)
        except ValueError:
            continue  # skip lines with non-integer stream values

        if (current_danceability == danceability) and (current_energy == energy):
            total_streams += streams
            total_count += 1
        else:
            if current_danceability is not None and current_energy is not None:
                row_key = "{}:{}".format(current_danceability, current_energy).encode()
                table.put(row_key, {
                    b'cf:total_streams': str(total_streams).encode(),
                    b'cf:total_count': str(total_count).encode(),
                    b'cf:mean_streams':str(total_streams/total_count).encode()
                })
                print("{0}\t{1}\t{2}\t{3}\t{4}".format(current_danceability, current_energy, total_streams, total_count,total_streams/total_count ))

            current_danceability = danceability
            current_energy = energy
            total_streams = streams
            total_count = 1

    # Final flush
    if current_danceability is not None and current_energy is not None:
        row_key = "{}:{}".format(current_danceability, current_energy).encode()
        table.put(row_key, {
            b'cf:total_streams': str(total_streams).encode(),
            b'cf:total_count': str(total_count).encode(),
            b'cf:mean_streams':str(total_streams/total_count).encode()
        })
        print("{0}\t{1}\t{2}\t{3}\t{4}".format(current_danceability, current_energy, total_streams, total_count,total_streams/total_count ))

except Exception as e:
    print("Processing error: {0}".format(e), file=sys.stderr)
    sys.exit(1)
finally:
    connection.close()
